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

def defie3():
    print("\n\tCONDITIONALS")
    print("Conditional statements (if, else, and elif) are fundamental programming constructs that allow you to control\nthe flow of your program based on conditions that you specify. They provide a\nway to make decisions in your program and execute different code based on those decisions.")
    
def defie3_code():
    print("\n•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    print("\nThe program will break if you enter a letter.")

    isOn = True
    sum=0

    while isOn == True:
        num = input("Enter a number: ")

        if num.isnumeric():
            sum += int(num)
        else:
            break
    print(f"The total is {sum}")

    print("\n\t-----\n\tINPUT\n\t-----")
    print()

    print('isOn = True\nsum = 0\n\nwhile isOn == True:\n   num = input("Enter a number: ")\n\n   if num.isnumeric():\n     sum += int(num)\n   else:\n     break\nprint(f"The total is {sum}")')

def nest():
	print("\nThe nested if statements in Python are the nesting of an if\nstatement inside another if statement with or without an else statement.")

def nest_code():
    print("\n•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------\nPurchasing an item program.")
    item_price = input("\nEnter the price of your item here: ")
    qty = input("How many did you buy? ")
    
    if item_price.isnumeric() and qty.isnumeric():
        total_price = int(item_price) * int(qty)
        if total_price >= 100:
            discount = total_price * 0.10
            discounted_price = total_price - discount
            print(f"Hello! We are happy to inform you that your purchase is discounted! The total price of your product is {total_price}. The discounted price is now {discounted_price}")
        else:
            print("You availed the original price")
    else:
        print("Please the numeric value of your purchase/s")
    
    print("\n\t-----\n\tINPUT\n\t-----")
    print('\nitem_price = input("Enter the price of your item here: ")\nqty = input("How many did you buy? ")if item_price.isnumeric() and qty.isnumeric():\n   total_price = int(item_price) * int(qty)\n   if total_price >= 100:\n     discount = total_price * 0.10\n     discounted_price = total_price - discount\n     print(f"Hello! We are happy to inform you that your purchase is discounted! The total price of your product is {total_price}. The discounted price is now {discounted_price}")\n   else:\n    print("You availed the original price")\nelse:\n   print("Please the numeric value of your purchase/s")')

def defi4():
    print("\n\tLOOPS")
    print("A loop is an instruction that repeats multiple times as long as some condition is met.")

def loopi():
    print("\n•For Loop - A for loop in Python is used to iterate over a sequence (list, tuple, set, dictionary, and string).")
    print()
    print("•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    for b in range (1, 8):
        print("\nROSE")
    print("\n\t-----\n\tINPUT\n\t-----")
    print('\nfor b in range (1, 8):\n   print("ROSE")')

def louwie():
	print("\nWhile Loop - The while loop is used to execute a set of statements as long as a condition is true.")

def nestie():
	print("\nNested For Loop - If a loop exists inside the body of another loop, it is called a nested loop.")
    
def nestie_code():
    print("\n•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    print()
    for a in range (0, 5):
        for b in range (0, 5-a):
            print(" ", end=" ")
        for c in range (0, 2*a+1):
            print("*", end=" ")
        print()
    print("\n\t-----\n\tINPUT\n\t-----")
    print('\nfor a in range (0, 5):\n   for b in range (0, 5-a):\n     print(" ", end=" ")\n   for c in range (0, 2*a+1):\n     print("*", end=" ")\n   print()')

def defie5():
    print("\n\tFUNCTIONS")
    print("A function is a block of code which only runs when it is called.")
    
def defie5_code():
    print("\nIn python, we create a function using the 'def' keyword.")
    print("\n•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    def hello():
        print("Hello, Good Day! How are you today?")
    hello()
    print("\n\t-----\n\tINPUT\n\t-----")
    print('def hello():\n   print("Hello, Good Day! How are you today?")\nhello()')

def defie6():
    print("\n\tLISTS")
    print("Lists are used to store multiple items in a single variable.")
    
def defie6_code():
    print("\n•••••• Example ••••••")
    print("\n\n\t------\n\tOUTPUT\n\t------")
    hi = ["hi" , "hello" , "hi"]
    print(hi)
    
    numbers = list(range(1,9))
    print(numbers)

    n = list("Alyssa Mae Dural Hufana")
    print(n)

    print("Processing")

    for x in n:
	    print(x, end="")
	
    print("\n\t-----\n\tINPUT\n\t-----")
    print('hi = ["hi", "hello", "hi"]\nprint(hi)\n\nn = list("Alyssa Mae Dural Hufana")\nprint(n)\n\nnumbers =list(range(19))\nprint(numbers)\n\nprint("Processing")\n\nfor x in n:\n   print(x, end="")')
    
def intro():
    print("\n\t~~~\n\tINTRODUCTION\n\t~~~")
    print("\nPython is a popular programming language. It was created by Guido van Rossum, and released in 1991. It is used for web development (server-side), software development, mathematics, and system scripting.")

def sub_intro():
    print("\n\t~~~\n\tOptions\n\t~~~")
    print("\n1 - Introduction\n2 - Back to main menu")
    
start = input("Hello, Good day! Would you like to start the program? (Yes / No): ")
if start.lower() == "yes":
    print("\nGreat! The program will now start. Please wait a little bit")
    menu()
else:
    print("\nThe program is now terminated Thank you for stopping by.")
    exit()
