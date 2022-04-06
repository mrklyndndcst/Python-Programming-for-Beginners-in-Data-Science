from os import system

# 45 function arguments

def avg_grades(*grades):
  for grade in grades:
    print(grade)
    
avg_grades(3.4, 4.0)

system('clear')

# 46 Python functions - Summary

# 47 Python Built-in Functions

string="testing"
print(len(string))

numbers = range(100)
print(len(numbers))

num = -28
print(abs(num))

name = "MarkLyndon"
# get first letter base on ascii code
print(f"lowest letter: {min(name)}\nhighest letter: {max(name)}")
list_numbers = range(1,100)
print(f"lowest number: {min(list_numbers)}\nhighest number: {max(list_numbers)}")

# 48 Python Built-in Functions Summary
python_built_in_function = "https://docs.python.org/3/library/functions.html"

