# Combine Logical operators

# characteristics of a probable candidate for a job opening
age = 21
qualification = "Bachelors"
experience = 2

# Let the variable "match" be a Logical variable. So, it takes a True or False.
# Write an if statement such that based on the following conditions the program should determine if the 
# candidate can be considered for a job interview or not. 

# The conditions are
# 1. candidates with at least an age of 21 and 
# 2. a qualification of either "Bachelors" or "Masters"  
# 3. and at least an experience of 2 years.


match = age >= 21 and (qualification == "Bachelors" or qualification == "Masters") and experience >= 2

print(match)