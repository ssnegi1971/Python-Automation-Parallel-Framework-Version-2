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
engine = create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')
query = "SELECT count(serialno) total_cnt, (select count(*) from dbo.etl_job_runs_depend where jobstatus = 'Success') cnt_success from dbo.etl_job_runs_depend;"
connection = engine.raw_connection();
cursor = connection.cursor();
df = pd.read_sql(query, engine);
#print (df);
for index, row in df.iterrows():
    if row.total_cnt != row.cnt_success:
        with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/keepprocessing.txt', 'w') as f:
            print("LOOP", file=f);
    else:
        with open('C:/Users/Admin/Desktop/work/Python/PythonAutomation/dependency/keepprocessing.txt', 'w') as f:
            print("STOP", file=f);
cursor.commit();
cursor.close();
#print("In check jobs");
#query = "SELECT * from dbo.grade;"
#df = pd.read_sql(query, engine);
#print (df);
