from os import system

# 75 What is Object Oriented Python

# 76-77 Write your first Python Class, attributes and methods in a class

class Account:
  def __init__(self, number):
    self.number = number

  def account_type(self):
    if str(self.number).startswith("1"):
      self.type = "current"
    elif str(self.number).startswith("2"):
      self.type = "saving"
      
  def interest_rate(self):
    self.account_type()
    
    if self.type == "current":
      self.interest = 0
    elif self.type == "saving":
      self.interest = 5
    return self.interest
  
acc_1 = Account(2001)
acc_2 = Account(1002)

print(acc_1.interest_rate())

print(isinstance(acc_1, Account))

system('clear')

