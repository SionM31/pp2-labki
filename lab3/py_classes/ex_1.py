# Define a class which has at least two methods: 

# 1) getString: to get a string from console input

# 2) printString: to print the string in upper case.

class Stringer:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = str(input("Input a string: "))
    
    def printString(self):
        print(self.string.upper())


x = Stringer()
x.getString()
x.printString()