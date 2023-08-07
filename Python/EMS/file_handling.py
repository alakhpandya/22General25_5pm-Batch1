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

f = open("ourBatch.csv")
data = f.readlines()
f.close()

stu = data[14]
print(stu)

# f = open("ourBatch.txt", "w")
# f.write("Hello World!")
# print(f.writable())
# f.writelines(data)
# f.close()

# CSV: Comma Seperated Values