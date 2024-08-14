# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pyodbc 
import pandas as pd 

conn = pyodbc.connect(driver='{SQL Server}',host='', 
                  database='Demo',Trusted_connection='yes')

qry1 = " select * from emp;"
df_emp= pd.read_sql_query(qry1, conn)

qry2="select * from dept;" 
df_dept=pd.read_sql(qry2, conn)

df_inner_join = pd.merge(left=df_emp, right=df_dept, how='inner', on='DEPTNO')



