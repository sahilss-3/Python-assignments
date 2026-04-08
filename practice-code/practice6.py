#to write data to file and read it back
data = input("enter text  to write in file: ")

with open("demo.txt", "w") as f:
    f.write(data)

print("Data written successfully")

print("Read From File: ")
with open("demo.txt", "r") as f:
    print(f.read())

f.close()