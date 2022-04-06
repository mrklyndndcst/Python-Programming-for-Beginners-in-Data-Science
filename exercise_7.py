# Find out if number is positive, negative or zero

number = int(input("Enter Any Number: "))

def answer(number):
  if number > 0:
    return "positive"
  elif number < 0:
    return "negative"
  else:
    return "zero"

value = answer(number)

print(value)