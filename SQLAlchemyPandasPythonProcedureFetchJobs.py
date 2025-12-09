import pyodbc
#import sqlalchemy as sa
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pandas as pd
import numpy as np
import sys
noofjobs=sys.argv[1];
server = "localhost\\SQLEXPRESS"
database = "NorthWind"
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server');
query = "SELECT count(*) cnt_jobs from dbo.etl_job_runs_depend where dependson in ('') and jobstatus in ('Ready','Fail');"
connection = engine.raw_connection()
cursor = connection.cursor()
df = pd.read_sql(query, engine);
for index, row in df.iterrows():
    if row.cnt_jobs==0:
        jobs_flag='D';
    else:
        jobs_flag='I';
print (jobs_flag);
if jobs_flag=='I':
    query = "SELECT top "+ noofjobs + " jobname from dbo.etl_job_runs_depend where dependson in ('') and jobstatus <> 'SUCCESS';"
    df = pd.read_sql(query, engine);
    lines = [];
    for index, row in df.iterrows():
        lines.append(row.jobname+"\n");
    with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonJobs.txt', 'w') as f:
        f.writelines(lines);
        print("null", file=f);
elif jobs_flag=='D':
    sql='''
    begin
declare @jobname varchar(100);
declare @jobstatus varchar(10);
declare jobscursor cursor for
select distinct jobname from (
select a.jobname, rank() over (partition by a.jobname order by b.jobstatus asc) rnk_jobs,
b.jobstatus
from (
SELECT
    jobname, s.value as Part
FROM
    [dbo].[ETL_Job_Runs_Depend] a
CROSS APPLY
    STRING_SPLIT(dependson, ',') AS s
    where jobstatus <> 'SUCCESS'
    and dependson <> '') a
inner join [dbo].[ETL_Job_Runs_Depend] b
on a.part = b.jobname
) a where jobstatus not in ('Ready', 'Fail') and rnk_jobs = 1;
open jobscursor;
fetch next from jobscursor into @jobname;
while @@FETCH_STATUS = 0
begin
update dbo.ETL_Job_Runs_Depend set RunFlag = 'Y' where jobname = @jobname;
fetch next from jobscursor into @jobname;
end;
CLOSE jobscursor;
DEALLOCATE jobscursor;
end;
'''
    cursor.execute(sql);
    cursor.commit();
    print ("Procedure Successful");
    query = "SELECT top "+ noofjobs + " jobname from dbo.ETL_Job_Runs_Depend where RunFlag = 'Y';"
    df = pd.read_sql(query, engine);
    lines = [];
    for index, row in df.iterrows():    
        lines.append(row.jobname+"\n");
    with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonJobs.txt', 'w') as f:
        f.writelines(lines);
        print("null", file=f);
    query = "update dbo.ETL_Job_Runs_Depend set RunFlag = '';";
    cursor.execute(query);
    cursor.commit();
cursor.close();
