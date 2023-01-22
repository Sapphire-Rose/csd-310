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

#beginning display
print("\n  Displaying Student Records...")

#Output collection 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#test document 
test_doc = {
    "student_id": "1010",
    "first_name": "Shaidar",
    "last_name": "Haran"
}

#Insert test student. 
test_doc_id = students.insert_one(test_doc).inserted_id

time.sleep(2)

#validate insertion 
print("\n  Insert Complete")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

#display inserted student
student_test_doc = students.find_one({"student_id": "1010"})

#Message for display
print("\n  Displaying Test Student Records")
print("  Student ID: " + student_test_doc["student_id"] + "\n  First Name: " + student_test_doc["first_name"] + "\n  Last Name: " + student_test_doc["last_name"] + "\n")

#delete test student
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

#find all students 
new_student_list = students.find({})

#display message 
print("\n  **Displaying all student records**")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  Done. Press any key to continue...")
