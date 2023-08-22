# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     pass

# f = open("myCollection.csv")
# print(f.read())
# print(f.closed)
# f.close()
# print(f.closed)

"""
with open("myCollection.csv") as f:     # same as f = open("ourBatch.csv")
    data = f.readlines()
    print(data[1])
print(f.closed)
"""
class ContextManager():
    
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        print("Enter method called")
        self.fp = open(self.path, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit method called")
        self.fp.close()
        print(exc_type)
        print(exc_value)
        print(traceback)


path = input("File name with full path: ")
mode = input("mode: ")
# f = ContextManager(path, mode)
with ContextManager(path, mode) as f:
    print("Code inside the with block executed")
    print(f.read())
    print(f.closed)
print(f.closed)