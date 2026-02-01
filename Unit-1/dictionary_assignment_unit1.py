# Create dictionary
student = {"name": "Rahul", "age": 18, "marks": 80}

# Access elements
print(student["name"])
print(student["age"])

# Update dictionary
student["marks"] = 90
print(student)

# Remove element
student.pop("age")
print(student)

# Merge dictionaries
extra = {"city": "Pune", "grade": "A"}
student.update(extra)
print(student)
