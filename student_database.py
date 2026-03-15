# Guided Implementations

# store the information with the state varibale 
student = {
    "name": "Dipak",
    "age": 21,
    "gpa": 3.6,
    "major": "Computer Science"
}

# print the student information. 
print("Name:", student["name"])
print("Age:", student["age"])
print("GPA:", student["gpa"])
print("Major:", student["major"])

# update gpa
student["gpa"] = 3.8
# print the update gpa
print("Updated student GPA: ",student["gpa"])

# Add new field
student["graduation_year"] = 2026

# Print all fields: 

for key in student:
    print(key, ":", student[key])

