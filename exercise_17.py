# Reverse a string
def reverse(name) :
  list_seq = list(reversed(name))
  string_seq = ''.join(map(str,list_seq))
  return string_seq

print(reverse("test"))