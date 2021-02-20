import pymysql

host = "localhost"
user = "root"
password = "root"
database = "bank"

def update(sql,param):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()

def find(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)
    cursor.close()
    con.close()

f=open("yonghushuju.txt","r+",encoding="UTF-8")
lis = f.readlines()
for i in lis:
    lis1 = i.replace("\n","").split(",")
    sql = "insert into username values(%s,%s,%s)"
    param = [lis1[0],int(lis1[1]),int(lis1[2])]
    update(sql, param)
f.close()

'''
sql= "select sum(money) from username"
param = []
data = find(sql,param)
sum = data[0][0]
print("净资产总额为：",sum)
'''

f = open("names.txt","w+",encoding="utf-8")
sql = "select * from username"
param = []
data = find(sql,param)
for i in data:
    string = ""
    string = string + i[0]
    string = string + "," + str(i[1])
    string = string + "," + str(i[2])
    f.write(string + "\n")
f.close()




'''
贾生,47,50000
"马云","58",1000000
"马化腾","57",1000202
"付光旭","20",560304
"穆子康","24",230023
"杜会朦","25",204892
'''