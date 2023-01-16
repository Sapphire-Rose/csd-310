from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.cgua3dr.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

print("\n Displaying Students")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
perrin = students.find_one({"student_id": "1009"})
print("\n Displaying Student - Find One")
print("  Student ID: " + perrin["student_id"] + "\n  First Name: " + perrin["first_name"] + "\n  Last Name: " + perrin["last_name"] + "\n")
