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
    query = "SELECT top "+ noofjobs + " jobname from dbo.etl_job_runs_depend where dependson in ('');"
    df = pd.read_sql(query, engine);
    lines = [];
    for index, row in df.iterrows():
        lines.append(row.jobname+"\n");
    with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonJobs.txt', 'w') as f:
        f.writelines(lines);
        print("null", file=f);
elif jobs_flag=='D':
    cursor.execute(f'exec [dbo].[Proc_Jobs_Cursor]');
    cursor.commit();
    print ("Procedure Successful");
    query = "SELECT top "+ noofjobs + " jobname from dbo.ETL_Job_Runs_Depend_current;"
    df = pd.read_sql(query, engine);
    lines = [];
    for index, row in df.iterrows():    
        lines.append(row.jobname+"\n");
    with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/pythonJobs.txt', 'w') as f:
        f.writelines(lines);
        print("null", file=f);
    query = "delete from dbo.ETL_Job_Runs_Depend_current;";
    cursor.execute(query);
    cursor.commit();
cursor.close();
