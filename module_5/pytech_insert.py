from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.cgua3dr.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
rand = {
    "student_id": "1007",
    "first_name": "Rand",
    "last_name": "al'Thor"
}
mat = {
    "student_id": "1008",
    "first_name": "Mat",
    "last_name": "Cauthon"
}
perrin = {
    "student_id": "1009",
    "first_name": "Perrin",
    "last_name": "Aybara"
}
students = db.students
print("\n  Inserting... ")
rand_student_id = students.insert_one(rand).inserted_id
print("  Inserted student record for Rand al'Thor into the students collection with document_id " + str(rand_student_id))

mat_student_id = students.insert_one(mat).inserted_id
print("  Inserted student record Mat Cauthon into the students collection with document_id " + str(mat_student_id))

perrin_student_id = students.insert_one(perrin).inserted_id
print("  Inserted student record Perrin Aybara into the students collection with document_id " + str(perrin_student_id))
