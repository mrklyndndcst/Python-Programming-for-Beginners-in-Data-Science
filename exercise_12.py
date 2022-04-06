# Nth Fibonacci Number

# What is the Fibonacci series ? It is a series of numbers in which each number ( Fibonacci number ) 
# is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

# Write a function fib (n) that takes in a number and returns the nth Fibonacci number

# The Correct way the 6th fibonacci number is 8

def fib(n) :
  num_1 = 0
  num_2 = 1
  fib_ser = []
  fib_ser.append(num_2)
  for i in range(n):
    num_3 = num_1 + num_2
    fib_ser.append(num_3)
    num_1 = num_2
    num_2 = num_3
  return fib_ser[n-1]

print(fib(int(input("Enter Any Number: "))))