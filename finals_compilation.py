__author__ = "ALYSSA MAE DURAL HUFANA"  
__course__ = "BSIT-2A"
__subject__ = "ITCS-102"
__year__ = "2024"

def p():
	print("\n•••••• Examples ••••••\n\n\t------\n\tOUTPUT\n\t------")
	print("Hello World")
	print("Alyssa")
	print("29")

def pri():
	print("\n\t-----\n\tINPUT\n\t-----")
	name = "Hello World"
	print(f"print('{name}')")
	
	namea = "Alyssa"
	print(f"print('{namea}')")
	
	num = "29"
	print(f"print('{num}')")

def menu():
	print("\n\t\t\t\t------------------------------------")
	print("\t\t\t\tWELCOME TO THE MENU OF COMPILATION")
	print("\t\t\t\t------------------------------------\n\nA compilation about PYTHON language. It is composed of different components in python such as variables, print statements, functions, loops, and many more.\nPython is a high-level, general-purpose programming language. This means it's designed to be easy to read and write, and it can be used for a wide variety of tasks. It's known for its clear syntax, which resembles natural language, making it easier for beginners to learn.\nIt's also very popular in the tech world, used for web development, data science, machine learning, scripting, and more. So, please fasten your seatbelt as we take a ride on this Python's journey. Hang on tight!")
	print("\n\n\t\t•Main Menu•")
	print()
	print("\t0 - Introduction \n\t1 - Print Statements\n\t2 - Operators\n\t3 - Conditionals\n\t4 - Loops\n\t5 - Functions\n\t6 - Lists\n\t7 - Exit")

def menu1():
    print("       \n\t•Main Menu•")
    print()
    print("0 - Introduction\n1 - Print Statements\n2 - Operators\n3 - Conditionals\n4 - Loops\n5 - Functions\n6 - Lists\n7 - Exit")
    
def sub1menu():
	print("\n\t----------------\n\tPRINT STATEMENTS\n\t----------------")
	print("\t1 - Definition\n\t2 - Code with examples\n\t3 - Back to main menu")

def sub2menu():
    print("\n\t---------\n\tOPERATORS\n\t---------")
    print("\t1 - Definition\n\t2 - Arithmetic Operators\n\t3 - Assignment Operators\n\t4 - Comparison Operators\n\t5 - Logical Operators\n\t6 - Back to main menu")
    
def sub3menu():
    print("\n\t------------\n\tCONDITIONALS\n\t------------")
    print("\t1 - Definition\n\t2 - Code with example\n\t3 - Nested Condition\n\t4 - Back to main menu")

def sub4menu():
    print("\n\t-----\n\tLOOPS\n\t-----")
    print("\t1 - Definition\n\t2 - For Loop\n\t3 - While Loop\n\t4 - Nested for Loop\n\t5 - Back to main menu")

def sub5menu():
    print("\n\t---------\n\tFUNCTIONS\n\t---------")
    print("\t1 - Definition\n\t2 - Code with Examples\n\t3 - Back to main menu")

def sub6menu():
	print("\n\t-----\n\tLISTS\n\t-----\n\t1 - Definition\n\t2 - Code with Examples\n\t3 - Back to main menu")

def defie1():
    print("\n\tPRINT STATEMENTS")
    print("Python print() function prints the message to the screen or any other standard output device.")

def defie2():
    print("\n\tOPERATORS")
    print("_Python Operators_\nOperators are used to perform operations on variables and values.")

def arith():
    print("\n\tARITHMETIC OPERATORS")
    print("Arithmetic operators are used with numeric values to perform common mathematical operations (+, -, , /, %, *, //)")
    print()
    print("•••••• Examples ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    print(200 + 52)
    print(6*5)
    print(7//7)
    print("\n\t-----\n\tINPUT\n\t-----")
    num1 = "200"
    num2 = "52"
    print(f"print({num1} + {num2})")
    num1 = "6"
    num2 = "5"
    print(f"print({num1}*{num2})")
    num1 = "7"
    num2 = "7"
    print(f"print({num1}//{num2})")

def assignn():
    print("\n\tASSIGNMENT OPERATORS")
    print("Assignment operators are used to assign values to variables 😊, +=, -=, *=, /=, etc.)")
    print()
    print("•••••• Examples ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    letter = ""
    a = input("Enter a letter: ")
    letter  += a 
    b = input("Enter a letter: ")
    letter  += b
    c = input("Enter a letter: ")
    letter  += c
    d = input("Enter a letter: ")
    letter  += d
    print(letter)
    print("\n\t-----\n\tINPUT\n\t-----")
    print('letter = " "\na = input("Enter a letter: ")\nletter += a\nb = input("Enter a letter: ")\nletter += b\nc = input("Enter a letter: ")\nletter += c\nd = input("Enter a letter: ")\nletter += d\nprint(letter)')

def compar():
    print("\n\tCOMPARISON OPERATORS")
    print("Comparison operators are used to compare two values (==, !=, <, >, <=, >=)")
    print()
    print("•••••• Examples ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    age = input("Enter your age:")

    if age.isnumeric():
	    if 12 >= int(age) >= 0:
		    print("Child")
	    elif 13 <= int(age) <=19:
		    print("Teen")
	    elif 20 <= int(age) <=59:
		    print("Adult")
	    elif 100 >= int(age) >=60:
		    print("Senior")
	    else:
		    print("Invalid input")
    print("\n\t-----\n\tINPUT\n\t-----")
    print('if age.isnumeric():\nif 12 >= int(age) >= 0:\n   print("Child")\nelif 13 <= int(age) <=19:\n   print("Teen")\nelif 20 <= int(age) <=59:\n   print("Adult")\nelif 100 >= int(age) >=60:\n   print("Senior")\nelse:\n   print("Invalid input")')
    
def logic():
    print("\n\tLOGICAL OPERATORS")
    print("Logical operators are used to combine conditional statements (and, or, not)")
    print()
    print("•••••• Examples ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    a = "Good"
    b = "Day"
    print(a and b)
    print(a or b)
    print(a and a)
    print("\n\t-----\n\tINPUT\n\t-----")
    print('a = "Good"\nb = "Day"\nprint(a and b)\nprint(a or b)\nprint(a and a)')
