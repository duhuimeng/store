import pymysql

con=pymysql.connect(host="localhost",user="root",password="root",database="company")
cursor=con.cursor()
#增
#sql="insert into t_dept values(%s,%s,%s)"
#param=['100','项目部','洛杉矶']

#删
#sql="delete from t_dept where deptno=%s"
#param=['100']

#改
#sql="update t_dept set loc=%s where deptno=%s"
#param=['西藏','50']

#查
sql="select * from t_dept where deptno=%s"
param=['40']

cursor.execute(sql,param)
date=cursor.fetchall()
print(date)
con.commit()
cursor.close()
con.close()
