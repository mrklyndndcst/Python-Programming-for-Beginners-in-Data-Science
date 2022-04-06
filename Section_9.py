from os import system

# 78-79  I/O - Input / Output

class Account:
  def __init__(self, number, name, balance):
    self.account_number = number
    self.account_name = name
    self.account_balance = balance
     
  def __str__(self): # summary
    return "Account " + str(self.account_name) + "'s bala nce is " + str(self.account_balance)
  
acc_1 = Account(1001, "Mark Decs", 100)

print(acc_1) 

text = "A tech is {} years old"
text_f = text.format(2)
print(text_f)

sample_text = "{test_1} is a {test_2} company".format(test_2 = "technology", test_1 = "ABC")
print(sample_text)

population = {
  "india": 135464684564,
  "china": 1684654984,
  "US": 25745419784
}

for key in population:
  print("The population in {} is {:,}.".format(key, population[key]))
  print(f"The population in {key} is {population[key]:,}.")
  print("{:<5} - {:>5}".format(key, population[key])) # with indentation
  
system('clear')
  
# 80 Execptions  

try:
  # file = open()
  test = "asdas"
  age = 1 + "1"
except Exception as e:
  print(repr(e))
  print("something is wrong")
finally:
  # file.close()
  print("hello")  

system('clear')

