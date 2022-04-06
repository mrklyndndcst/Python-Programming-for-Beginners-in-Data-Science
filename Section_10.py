from math import ceil, floor, trunc
from os import system

# 81 Date Object
from datetime import date, timedelta

date_test =  date (2019, 12, 18)
today = date.today()

print(date_test.day)
print(date_test.month)
print(date_test.year)
print(today.weekday()) # mon - 0 .... sun - 6

print(today.strftime("%Y-%m-%d")) #string format time

system('clear')

# 82 Quiz Discusion

print(today.strftime("%b '%y"))
print(today.strftime("%W"))
print(date_test - today)

system('clear')

# 84 Time delta

tomorrow = today + timedelta(days = 1)
print(tomorrow) 

thre_weeks = today + timedelta(weeks = 3)
print(thre_weeks)

birthday = date(1992, 6, 30)
birthday = birthday.replace(year = today.year)
print(birthday - today)

system('clear')

# 85 Time Object
import time

before = time.time()

sum = 0
for i in range (1000):
  sum += i
  
after = time.time()

print(after - before)

today = time.localtime()
print(today)

system('clear')

# 85 Date time

from datetime import datetime

today = datetime.now()
print(str(today))
print(today.minute)
print(today.strftime("%b-%d-%Y"))

date_string = 'Dec-18-2019'
print(type(date_string))
date_format = datetime.strptime(date_string, "%b-%d-%Y")
print(type(date_format))

system('clear')

# 86 File Operations - Read files

f = open("sample.txt", "r") # open file
print(f.read()) # read all
print(f.readline()) # read line

for line in f:
  print(line)

f.close()

system('clear')

# 87 File Operations - Write and Append Files

f = open("Screen Shot 2022-04-01 at 11.32.15 AM.png", "rb")
data = f.read()
f.close()

fw = open("Screen Shot copy.png", "wb") # copy
fw.write(data)
fw.close()

f = open("sample.txt", "r") # open file
data = f.read()

fw = open("sample copy.txt", "a") 

fw.write(data)
fw.write("\nadditional message")

fw.close()

system('clear')

# 88 File Operations - Exception Handling

try:
  f = open ("non existing.txt", "r")
except Exception as e:
  print(repr(e))
  print("not existing file")
finally:
  f.close()
  
# with open("non existing file", "r") as f:
#   test = 1/0

system('clear')

# 89 Math Module
from math import exp, sqrt, log, pi, e, radians, sin, fsum

i = 3.1
print(ceil(i))
j = 3.9
print(floor(j))

i = -3.57
print(trunc(i)) # remove decimal part

i = 2
print(exp(i))

print(5 ** 2)
print(pow(6,2))

print(sqrt(81))

print(log(100)) # base of e (e)
print(log(100,10)) # base of 10

print(pi)

print(e)

sin(radians(90))

num_1 = [1,2,3,4,5]
print(fsum(num_1))