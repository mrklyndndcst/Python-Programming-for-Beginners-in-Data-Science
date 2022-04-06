# Odd numbers between 1 and 20

# Find all the odd numbers between 1 and 20. Append them to a string with spaces in between. Like so

# odd_numbers = "1 3 5 7 9 11 13 15 17 19" 

odd_numbers = ""
 
for x in range(1,21):
  if x%2 == 1:
    if not odd_numbers:
      odd_numbers += str(x) 
    else:
      odd_numbers += " " + str(x) 
            
print(odd_numbers)            