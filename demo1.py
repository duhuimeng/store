import pymongo
import requests


# response = requests.post(url="http://www.jasonisoft.cn:8080/HKR/UserServlet?method=findAllStudent")
# response.encoding = "utf-8"

client = pymongo.MongoClient("mongodb://localhost:27017")
lists = client.list_database_names()
db = client["student"]
#删
#users = {"username":"郭德纲"}
#db["学生数据"].delete_one(users)
#增
# data = response.json()
# for i in data:
#    status = db["学生数据"].insert_one(i)
#改
# use = {"username":"王瑞敏"}
# use1 = {"$set":{"username":"王"}}
# db["学生数据"].update_one(use,use1)
#查
use = {}
# status = db["学生数据"].find_one(use)
# print(status)
#response = requests.post(url="http://www.jasonisoft.cn:8080/HKR/CourseServlet?method=findAllCourse")
#response.encoding = "utf-8"
#data = response.json()
#for i in data:
#    db["课程管理"].insert_one(i)
a = 0
for i in db["学生数据"].find():
    if i["classname"] == "测试开发":
        a = a + 1
print(a)
# for i in db["学生数据"].find().limit(10000):
#     print(i)