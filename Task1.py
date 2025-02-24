# Task NO 1:
""" i) Create a Python script that declares the variable in which print All information
       about yourself like (name,gender,age,Address,degree,dob and necessary
       information) """

# Declaring variables for personal information
name = "Faisal Rafiq"
gender = "Male"
age = 22
address = "123 Main Street, Lahore"
degree = "BS in Software Engineering"
dob = "2000-03-31"
email = "faisal@example.com"
phone = "+92 111 234 5678"

# Printing all info about myself using fstring.
print(f"""
=== Personal Information ===
Name        : {name}
Gender      : {gender}
Age         : {age}
Address     : {address}
Degree      : {degree}
DOB         : {dob}
Email       : {email}
Phone       : {phone}
""")




""" 
ii) Write a Python script that demonstrates type casting while swapping two variables. And print
Before and After Swapping

"""

# Initial values
a = 10  # Int
b = 5.5  # Float

print("Before Swapping:")
print(f"a = {a} (Type: {type(a)})")
print(f"b = {b} (Type: {type(b)})")

# Swapping with type casting
a, b = float(a), int(b)

print("\nAfter Swapping:")
print(f"a = {a} (Type: {type(a)})")
print(f"b = {b} (Type: {type(b)})")


""" 
iii) Declared a Variable With different Data Types in Python and display along
variable with data types.

"""
# Declaring variables with different data types
a = 100
b = 10.5
c = "Hello, World!"
d = True
e = [1, 2, 3, 4, 5]
f = (10, 20, 30)
g = {"name": "Faisal", "age": 22}
h = {1, 2, 3, 4, 5}
i = 3 + 4j

# Display variables along with their data types 
print(f"""
=== Variables and Their Data Types ===
Integer Variable  : {a} (Type: {type(a)})
Float Variable    : {b} (Type: {type(b)})
String Variable   : {c} (Type: {type(c)})
Boolean Variable  : {d} (Type: {type(d)})
List Variable     : {e} (Type: {type(e)})
Tuple Variable    : {f} (Type: {type(f)})
Dictionary Variable: {g} (Type: {type(g)})
Set Variable      : {h} (Type: {type(h)})
Complex Variable  : {i} (Type: {type(i)})
""")


# TASK NO 2:

""" i) 
Write a Python script using two variables and perform the following operations Addition,
Subtraction, Multiplication, Division, Modulo

"""

# Defining two variables
a = 20
b = 10

# Performing arithmetic operations and printing results
print(f"""
=== Arithmetic Operations ===
Addition       : {a} + {b} = {a + b}
Subtraction    : {a} - {b} = {a - b}
Multiplication : {a} * {b} = {a * b}
Division       : {a} / {b} = {a / b}
Modulo         : {a} % {b} = {a % b}
""")



""" ii) Using Two Numerical Variables and Write a Python Scripts to Compare them using Comparison
Operators

"""

# Defining two numerical variables
x = 6
y = 31

# Comparing the variables and printing results
print(f"""
=== Comparison Operations ===
{x} == {y} : {x == y}
{x} != {y} : {x != y}
{x} > {y}  : {x > y}
{x} < {y}  : {x < y}
{x} >= {y} : {x >= y}
{x} <= {y} : {x <= y}
""")


""" iii) Write a Python script that demonstrates the use of assignment operators.

"""
# Initialize variables
a = 6
b = 31

# Perform assignment operations
add = a + b  # Addition assignment
sub = add - b  # Subtraction assignment
mul = sub * b  # Multiplication assignment
div = mul / b  # Division assignment
floor_div = mul // b  # Floor division assignment
mod = mul % b  # Modulus assignment
exp = b ** 2  # Exponentiation assignment

# Print results in one statement
print(f"The values of a and b is: {a} , {b}")

print(f"""
    Addition: {add}
    Subtraction: {sub} 
    Multiplication: {mul}
    Division: {div}
    Floor Division: {floor_div}
    Modulus: {mod}                
    Exponentiation: {exp}


NOTE:  a = a % b = 186 % 31 = 0 (186 is exactly divisible by 31) (USING PREVIOUS VALUES - if we want all separate just print sep..)
""")


""" iv) Write a Python script to demonstrate the use of logical operators. Your script
should perform the following tasks:
1. Define Boolean Variables
2. Evaluate Logical Conditions
3. Output the Results

"""
# Defining Boolean Variables
a, b = True, False

# Evaluating Logical Conditions and Printing Results
print(f"""
=== Logical Operators ===
a = {a}, b = {b}

a AND b  : {a and b}
a OR b   : {a or b}
NOT a    : {not a}
NOT b    : {not b}

NOT = Reverse the original answer
""")