# myfile = open("fruits.txt")
# print(myfile.read())
# myfile.close()

# with open('/Users/femitemiola/Desktop/programs/vegetables.txt', 'w') as myfile:
#     myfile.write("Tomato\nCucumber\nOnion")



# myfile = open("fruits.txt")


# def character(char, filepath="bear.txt"):
#     file = open(filepath)
#     content = file.read()
#     return content.count(char)

# print(myfile.count("apple"))

# myfile = open("bear.txt")
# content = myfile.read()
# for char in content:
#     x = char[:90]
# first =  open("first.txt", "w")  
# first.write("x")
  
# first.close()

# # This is how to write the first 90 characters in an exist file
# with open("bear.txt") as file:
#     content = file.read()
# with open("first.txt", "w") as file:
#     file.write(content[:90])

# how to read and write in file
with open('fruits.txt', 'a+') as myfile:
    myfile.write("\ntomatoes")
    myfile.seek(0) # this code helps to bring the cursor in the file back to the zero position
    content = myfile.read()

print(content)

# how to append file to another file 
with open("bear1.txt", "r") as file:
    content = file.read()

with open("bear2.txt", "a") as file2:
    file2.write(content)




