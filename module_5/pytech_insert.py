#import
from pymongo import MongoClient

#Mongo connection string
url = "mongodb+srv://admin:admin@cluster0.cgua3dr.mongodb.net/pytech?retryWrites=true&w=majority"

#Mongo Connection cluster
client = MongoClient(url)

#pytech database
db = client.pytech

#student documents
rand = {
    "student_id": "1007",
    "first_name": "Rand",
    "last_name": "al'Thor",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Swords and Sword Accessories",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "The Art of Magic",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                }
            ]
        }
    ]
}

mat = {
    "student_id": "1008",
    "first_name": "Mat",
    "last_name": "Cauthon",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Swords and Sword Accessories",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "The Art of Magic",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                }
            ]
        }
    ]
}

perrin = {
    "student_id": "1009",
    "first_name": "Perrin",
    "last_name": "Aybara",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "CSD310",
                    "description": "Swords and Sword Accessories",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                },
                {
                    "course_id": "CSD320",
                    "description": "The Art of Magic",
                    "instructor": "Professor Merrilin",
                    "grade": "A+"
                }
            ]
        }
    ]
}

#student collection
students = db.students

#insert statements
print("\n  Inserting... ")

rand_student_id = students.insert_one(rand).inserted_id
print("  Inserted student record for Rand al'Thor into the students collection with document_id " + str(rand_student_id))

mat_student_id = students.insert_one(mat).inserted_id
print("  Inserted student record Mat Cauthon into the students collection with document_id " + str(mat_student_id))

perrin_student_id = students.insert_one(perrin).inserted_id
print("  Inserted student record Perrin Aybara into the students collection with document_id " + str(perrin_student_id))
