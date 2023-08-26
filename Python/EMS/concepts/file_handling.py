"""
f = open("C:\\Users\\Alakh Pandya\\Desktop\\Batches\\22General25_5pm-Batch1\\Python\\EMS\\ourBatch.txt")

data = f.read()
print(data)

# print(type(data))

# data1 = f.read(12)
# print(data1)

print(f.tell())

f.seek(20)

data2 = f.read(20)
print(data2)

print(f.tell())

# f.readline()
# row = f.readline()
# print(row)

data = f.readlines()
# print(data[5])
new = '20\tDhiraj\t\tOwner'
data.append(new)
print(data)
"""
# f.write("Hello World!")
# print(f.writable())
# print(f.readable())
# f.close()

# File Opening syntax:
# f = open("file_name with extension and full path", "Mode1Mode2")
"""
Mode 1  Name            Description                                         Mode2   Name
r       read            Opens the file for reading only                     t       text        Default
                        Cursor is placed at the begining of the file
                        (Reading will start from the begining)
                        Does not erase the content of the file
                        Raises FileNotFoundError if the file does not exist

w       write           Opens the file for writing only                     b       binary
                        Erases entire content of the file at the time of opening
                        Creates the file if it does not exist
                        Places the cursor at the begining of the file

a       append          Opens the file for writing only
                        Does not erase the content of the file
                        Creates the file if it does not exist
                        Places the cursor at the end of the file

x       Exclusively     Creates the file and opens it for writing only if it does not exist
        Create          Raises FileExistsError if the file already exists
                        Places the cursor at the begining of the file

r+      read plus       Opens the file for reading & writing both
                        Cursor is placed at the begining of the file
                        (Reading will start from the begining)
                        Does not erase the content of the file
                        Raises FileNotFoundError if the file does not exist

w+      write plus      Opens the file for reading & writing both
                        Erases entire content of the file at the time of opening
                        Creates the file if it does not exist
                        Places the cursor at the begining of the file

a+      appnd plus      Opens the file for reading & writing both
                        Does not erase the content of the file
                        Creates the file if it does not exist
                        Places the cursor at the end of the file
"""
"""
# f = open("ourBatch.txt")    # is same as writing f = open("ourBatch.txt", "rt")
f = open("ourBatch.txt")
data = f.readlines()
f.close()

new = "20\tDhiraj\t\tOwner\n"
data.append(new)

f = open("ourBatch.txt", "w")
# f.write("Hello World!")
# print(f.writable())
f.writelines(data)
f.close()
"""

# f = open("ourBatch.txt", "a")
# f.write("21\tRahul\t\tJava\n")
# f.close()

# f = open("yourBatch.txt", "x")
# f.close()

# f = open("ourBatch.txt", "r+t")
# f.write("Some text")
# f.close()
"""
f = open("ourBatch.csv")
data = f.readlines()
f.close()

stu = data[14]
print(stu)
"""
# f = open("ourBatch.txt", "w")
# f.write("Hello World!")
# print(f.writable())
# f.writelines(data)
# f.close()

# CSV: Comma Seperated Values
"""
f = open("ourBatch.csv", "a+t")
# f.write("22,Krupa,Student\n")
f.seek(0)
print(f.read())
f.close()
"""
'''
f = open("ourBatch.csv", "r")
data = f.readlines()
f.close()
print(data)

while True:
        print("Press 1 to add a new student")
        print("Press 2 to see details of an existing student")
        print("Press 3 to update details of a student")
        print("Press 4 to delete a student")
        print("Press 9 to exit")
        ch = int(input())

        if ch == 1:
                print("Enter the following details:")
                sr = str(len(data))
                name = input("Name: ")
                role = input("Role: ")

                if "\n" in data:
                        sr = data.index("\n")
                        data.pop(sr)
                        data.insert(sr, f"{str(sr)},{name},{role}\n")
                else:
                        data.append(f"{sr},{name},{role}\n")

        elif ch == 2:
                sr = int(input("Sr no: "))
                student_info = data[sr].split(",")
                sr, name, role = student_info
                role = role.rstrip()
                print(f"------------ Info of sr no:{sr} ------------")
                print("Name:", name)
                print("Role:", role)

        elif ch == 3:
                sr = int(input("Sr no: "))
                student_info = data[sr].split(",")
                sr2, name, role = student_info
                role = role.rstrip()
                print(f"------------ Update details of sr no: {sr} ------------")
                print("Field\tOld\tNew".expandtabs(10))
                new_name = input(f"Name\t({name}):\t".expandtabs(10))
                new_role = input(f"Role\t({role}):\t".expandtabs(10))
                data.pop(sr)
                data.insert(sr, f"{str(sr)},{new_name},{new_role}\n")

        elif ch == 4:
                sr = int(input("Sr no: "))
                removed_student = data.pop(sr)

                # shifting serial nos of rest of all:
                """
                for i in range(sr, len(data)):
                        temp = data[i].split(",")
                        data.pop(i)
                        new_sr = int(temp[0]) - 1
                        temp[0] = str(new_sr)
                        data.insert(i, (",".join(temp)))
                """
                
                # inserting null string in place of removed student
                data.insert(sr, "\n")
                print(f"{removed_student.split(',')[1]} has been removed successfully...")

        elif ch == 9:
                f = open("ourBatch.csv", "w")
                f.writelines(data)
                f.close()
                break

        else:
                print("Invalid option, please try again...")
'''

"""
f = open("myCollection.csv")
data = f.readlines()
f.close()

sr = int(input("Sr no: "))
album_info = data[sr].split(",")

print("Artist:", album_info[1])
print("Album Name:", album_info[2])
"""

import csv

f = open("myCollection.csv")
# data = list(csv.reader(f))
# for row in data:
#     print(row)

# title = data.pop(0)
# print(title)
# print(data)

data = csv.reader(f)
title = next(data)
print(title)
print(list(data))
f.close()