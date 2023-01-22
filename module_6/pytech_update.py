#import
from pymongo import MongoClient

#import
import time

#Mongo connection string
url = "mongodb+srv://admin:admin@cluster0.cgua3dr.mongodb.net/pytech?retryWrites=true&w=majority"

#Mongo Connection cluster
client = MongoClient(url)

#pytech database
db = client.pytech

#student collection
students = db.students

#find all students in the collection 
student_list = students.find({})

#display message 
print("\n  Displaying Students from Documents...")

#output results
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Trakand"}})

#find the updated student document 
rand = students.find_one({"student_id": "1007"})

#display messages
print("\n Processing update...")
time.sleep(2)
print("\n  **Display Updated Student ID 1007**")

#updated output
print("  Student ID: " + rand["student_id"] + "\n  First Name: " + rand["first_name"] + "\n  Last Name: " + rand["last_name"] + "\n")

#exit 
input("\n\n  Done. Press any key to continue...")
