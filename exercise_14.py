# Sum of all alternate odd numbers:

def alternate_odd(n):
  total = 0
  add = True
  for i in range(n + 1):
    if i % 2 != 0:
      if add:
        total += i
        add = False
      else:
        add = True
  return total

print(alternate_odd(13))
    