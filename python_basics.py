# ==============================
# Day 2 - Python Basics
# Variables, Data Types, Operators,
# Loops, Functions & Simple Programs
# ==============================

print("===== DAY 2 - PYTHON BASICS =====\n")

# -------------------------------
# 1. Variables
# -------------------------------
print("1. Variables")

name = "Kanchan"
age = 21
cgpa = 8.72

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)

print("\n-------------------------------")

# -------------------------------
# 2. Data Types
# -------------------------------
print("2. Data Types")

integer = 100
floating = 25.75
text = "Data Science"
boolean = True
my_list = [10, 20, 30]
my_tuple = ("Python", "SQL")
my_set = {1, 2, 3}
my_dict = {"Name": "Kanchan", "Course": "AI & ML"}

print("Integer:", integer)
print("Float:", floating)
print("String:", text)
print("Boolean:", boolean)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dictionary:", my_dict)

print("\n-------------------------------")

# -------------------------------
# 3. Operators
# -------------------------------
print("3. Operators")

a = 20
b = 5

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Power:", a ** b)

print("\nComparison Operators")
print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)

print("\nLogical Operators")
print(True and False)
print(True or False)
print(not True)

print("\n-------------------------------")

# -------------------------------
# 4. Input & Output
# -------------------------------
print("4. Input and Output")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Welcome", user_name)
print("Your age is", user_age)

print("\n-------------------------------")

# -------------------------------
# 5. If-Else
# -------------------------------
print("5. If Else Statement")

if user_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n-------------------------------")

# -------------------------------
# 6. For Loop
# -------------------------------
print("6. For Loop")

for i in range(1, 6):
    print("Number:", i)

print("\n-------------------------------")

# -------------------------------
# 7. While Loop
# -------------------------------
print("7. While Loop")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1

print("\n-------------------------------")

# -------------------------------
# 8. Functions
# -------------------------------
print("8. Functions")

def greet(name):
    print("Hello,", name)

greet(user_name)

def add(x, y):
    return x + y

result = add(15, 25)

print("Addition using Function:", result)

print("\n-------------------------------")

# -------------------------------
# 9. Simple Program - Even or Odd
# -------------------------------
print("9. Even or Odd")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("\n-------------------------------")

# -------------------------------
# 10. Multiplication Table
# -------------------------------
print("10. Multiplication Table")

table = int(input("Enter a number for table: "))

for i in range(1, 11):
    print(f"{table} x {i} = {table*i}")

