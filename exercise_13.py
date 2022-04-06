#  Sum of numbers divisible by 5 between andy two given numbers

#Write a function that takes in 2 numbers. Find out all the numbers divisible by 5 between those numbers and add them up. Return the sum.

def sum_numbers(n,m) :
  if n > m:
    max_num = n + 1
    min_num = m
  else:
    max_num = m + 1
    min_num = n
  total = 0
  
  for i in range(min_num, max_num):
    if i % 5 == 0:
      total += i
  return total

print(sum_numbers(int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: "))))