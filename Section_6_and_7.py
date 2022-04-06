from os import system

# 49 What are list

# 50 Challenge: Find out how many vowels are in a given sentence

sentence = "This is a good sentence."
vowels = [ "a", "e", "i", "o", "u"]
count = 0
for i in sentence:
  if i in vowels:
    count += 1
print(count)

# 51 List Indexing and Merging
a = [1, 3, 5]
b = [7, 9, 11]
a.extend(b)
list_sampe = [1 ,2 ,3, 4, 5]
# indexing
print(list_sampe[3])
# negative indexing
print(list_sampe[-2])

#52 List Manipulation
list_52 = [1, 2, 3, 4, 5]
list_52.insert(2, 7) # insert
print(list_52)
list_52[4] = 9 # replace the specific element
print(list_52)
list_52.pop() # remove last item if not specified nth element
print(list_52)
list_52.remove(3) # remove the specific element
print(list_52)
system('clear')

# 53-55 Challenge: Average Grade

grades = []
while False: #change to True to run
  print("Enter your Choices")
  print("Enter grades - 1 ->")
  print("List grades - 2 ->")
  print("Delete grades - 3 ->")
  print("Edit grades - 4 ->")
  print("Clear grades - 5 ->")
  print("Exit Program - 6 ->")
  print("Calculate Average - 7 -")
  
  choice = input("->")
  if choice.isnumeric() and int(choice) in range(1, 8):
    choice = int(choice)
    pass
  else:
    print('not a valid choice, again')
  
  if choice == 6:
    break
  
  if choice == 1:
    print("Enter grades")
    
    while True:
      grade = input("->")
      
      if grade == "e":
        break
      elif not grade.isnumeric():
        print("Not Valid grade, Enter grade again")
      else: 
        grade = float(grade)
        grades.append(grade)
        
  if choice == 2:
    for i in grades:
      print(i)
  
  if choice == 3:
    for i in grades:
      print(i)
    print("enter the index to delete ")
    index = int(input( "->"))
    if index < len(grades) - 1 and index >= 0:
      grades.pop(index)
    else:
      print("invalid index try again")
      
  if choice == 4:
    for i in grades:
      print(i)
    print("enter the index to update")
    index = int(input( "->"))
    if index < len(grades) - 1 and index >= 0:
      print("enter new grade")
      new_grade = float(input("->"))
      grades[index] = new_grade
    else:
      print("invalid index try again")
  
  if choice == 5:
    grades.clear()
    
  if choice == 7:
    ave = sum(grades)/(len(grades))
    print(f"average = {ave}")

# 56 Nested List

person = [["Adam", "Smith"], 25, 160.65]

# 57 Enumerate Lists

e = enumerate(person)

for i in e:
  print(i)
  
system('clear')

# 58 Merge and Sorlt Lists

list_58_odd = [1, 3, 5, 7, 9]
list_58_even = [2, 4, 6, 8, 10]

all_list_58 = list_58_odd + list_58_even

print(all_list_58)

all_list_58.sort()
print(all_list_58)

system('clear')

#  59 List Slicing

list_59 = [2, 3.4, 2.3, 3.4, 4.0, 3.1, 1.2]

print(list_59[3 : 5])
print(list_59[3:])

system('clear')

# 60 Python Dictionary

dict_60 = {"math": 4.0, "english": 3.0}
print(dict_60["math"])

dict_60["math"] = 3.5 # changing elements

dict_60["science"] = 4.0 # adding elements

system('clear')

# 61 get vs index

dict_61 = {"math": 4.0, "english": 3.0}

print(dict_61.get('math'))
dict_60["science"] = 3.5 # return error
print(dict_61.get('science')) # return none

system('clear')

# 62 Challenge - Vowels

sentence = "This is a good sentence."
vowels = [ "a", "e", "i", "o", "u"]
count = {}
for i in sentence:
  if i in vowels:
    if count.get(i) == None:
      count[i] = 1
    else:
      count[i] += 1

print(count)

system('clear')

# 63 Dictionary access

dict_62 = {"math": 4.0, "english": 3.0}

print(dict_62.get('science', ''))

system('clear')

# 64 Dictionary - Key and Value objects

dict_63 = {"math": 4.0, "english": 3.0}

for key in dict_63:
  print (key, dict_63[key])
  
print(dict_63.keys())
print(dict_63.values())

system('clear')

# 65 Challenge: Find out the list of all words that contaon a particular vowel

sentence_65 = "This is all i've got a good sentence and one of a kind."
words = sentence_65.split()
vowels = [ "a", "e", "i", "o", "u"]
result = {}

list_words_with_count = []

for word in words:
  for letter in vowels:
    if letter in word:
      if result.get(letter) == None:
        result[letter] = [word]
      else:
        result.get(letter).append(word)

print(result)

system('clear')

# 66-67  list words from sentence in number of occurnces in reverse

sentence_66 = "This is all i've got a good sentence and one of a kind which also added three words of a and two words of one."
sentence_66 = sentence_66.replace('.','')
words = sentence_66.split()
count_occurences = {}

for word in words:
  if count_occurences.get(word) == None:
    count_occurences[word] = 1
  else:
    count_occurences[word] += 1

list_count_occurences = []

for i, j in count_occurences.items():
  list_count_occurences.append([i, j])

def sort_criteria(ls):
  return ls[1]

list_count_occurences.sort(key = sort_criteria, reverse = True)

print(list_count_occurences)

system('clear')

# 68 Dictionary - Deletion

dict_68_a = {"math": 4.0, "english": 3.0}
dict_68_b = {"math": 3.0, "science": 4.0, "history": 3.0}

dict_68_a.update(dict_68_b) # update
del dict_68_a["history"] # delete
dict_68_a.pop("english") # delete

print(dict_68_a)

system('clear')

# 69-70 Python Tuples

numbers = ([1,3,4], [7,9,11])
list_69 = ('one', 'two', 'one')
print(list_69[0])
print(type(list_69))

print(list_69.count('one'))

ages_tuple = (4,5,7,3,5,6,8,5,8,5)
ages_list = [4,5,7,3,5,6,8,5,8,5]

def schools (age):
  if 11>= age >= 5:
    return True
  else:
    return False

primary_schools = filter(schools, ages_list)

for age in primary_schools:
  print(age)
    
system('clear')

# 71 Python Sets

weather = {'rainy', 'sunny'}
weather.add("stormy") # add
weather.remove("rainy") # remove element
weather.pop() # remove random element
print(weather)
weather.clear() # remove all
print(weather)

system('clear')

# 72-73 Set Operations (Union, Intersection, Difference etc.)

odd_num_1 = {1,3,5,7}
odd_num_2 = {7,9,11,13,15}

union = odd_num_1.union(odd_num_2) # combined
union = odd_num_1 | odd_num_2 # combined
print(union)

intersection = odd_num_1.intersection(odd_num_2) # get only identical
intersection = odd_num_1 & odd_num_2 # get only identical
print(intersection)

difference = odd_num_1.difference(odd_num_2) # remove only identical
difference = odd_num_1 - odd_num_2 # remove only identical
print(difference)

symmetric = odd_num_1.symmetric_difference(odd_num_2) # remove identical
symmetric = odd_num_1 ^ odd_num_2 # remove identical
print(symmetric)

odd_num_1.discard(1) # remove specific element
print(odd_num_1)

system('clear')

# 74 Python Sets - Summary
