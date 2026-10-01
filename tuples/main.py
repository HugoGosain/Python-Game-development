
list1=["red",75,12.5,"yes"]


# dictionary1={
#     "name": "Alex",
#     "age": 14,
#     "hobby": "piano",
#     "favouritecolor": "green"
# }

# print (list1)
# print (dictionary1)

# Tuples:

# tuple1 = ("red", 75, 12.5, "yes", [9,8,7], list1)

# print (tuple1[1])

# tuple1[4][2] = 5

# print (tuple1)

studentlist=[]
for j in range(5):
    print(f"\nEnter details for group {j+1}:")
    name1 = input("What is your group name? ")
    size1 = input("What is the size of your group? ")
    date1 = input("What was the date of your competition? ")
    venue1 = input("What was your venue? ")
    medal1 = input("What medal did you get? ")

    groupdetails=(name1,size1,date1,venue1,medal1)

    studentlist.append(groupdetails)
    for i in studentlist:
        print (i)