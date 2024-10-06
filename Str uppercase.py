class IOString():

    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input("Enter String : ")

    def print_String(self):
        print("Result is :", self.str1.upper())


strObj = IOString()

strObj.get_String()
strObj.print_String()