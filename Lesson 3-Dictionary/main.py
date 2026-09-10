student = {"name": "Alex",
           "age":12,
           "grade":7,
           "country":"USA"
           }
# accessing values
print(student["name"])
# add a new key
student["hobby"]="football"
print(student)
# update an existing value
student["grade"]=8
print(student)
# checking if key exists
# you can use "not in" instead of in to find find things that are not in the dictionary
if "age" in student:
    print("found it")
else:
    student["age"]=12
    print (student)
print(student.get("grade"))
# looping through a dictionary
for item in student:
    print (item)
# keys()
print(student.keys())
for item in student.values():
    print (item)
for item in student.items():
    print (item)