# First Prime Numbers between a given range of numbers

def first_prime (number_1, number_2):
  min_num = min(number_1, number_2)
  max_num = max(number_1, number_2)
  checker = 0
  n = 15
  for i in range(min_num, max_num + 1):
    for x in range(1 , i + 1):
      if i % x == 0:
        checker += 1
    if checker == 2:
      return i
    else:
      checker = 0
      
print(f"The first prime number {first_prime(8, 50)}")       
      
        
    
