from os import system

# 90 What is NumPy

# 91 What makes NumPy faster

# 92 How to create Arrays in NumPy
 
import numpy as np

a = [1,2,3,4,5,6,7,8,9,10]
b = [11,12,13,14,15,16,17,18,19,20]
print(np.array(a))

c = np.array([a, b])
print(c)

system('clear')

# 93 How to Reshape Numpy Arrays
 
print(c.shape) 

n = np.arange(1,13)
print(n)
print(n.reshape(4,3))
print(n.reshape(2,6))

system('clear')

# 94 Element wise operations in NumPy

a = np.array([1,2,3])
print(a * 3)
b = np.array([4])
print(a + b)

system('clear')

# 95 Agregrate Operations in NumPy

a = np.array([[1,2,3],[4,5,6]])
print(np.sum(a, axis=1))
print(np.min(a, axis=0))

system('clear')

# 96 Array Indexing in NumPy

a = [1,2,3,4,5,6]
print(a[0])

b = np.array([a, [7,8,9,10,11,12]])
print(b[1,2])

system('clear')

# 97 Array Slicing in NumPy

a = np.array([1,2,3,4,5,6,7,8,9,10])
print(a[3:7])

b = np.array([
  [ 1, 2, 3, 4],
  [ 5, 6, 7, 8],
  [ 9,10,11,12],
  [13,14,15,16]
])

print(b[1:3,1:4])

system('clear')

# 98 Append rows/columns in NumPy

a = np.array([
  [ 1, 2, 3, 4, 5],
  [ 6, 7, 8, 9,10],
  [11,12,13,14,15],
  [16,17,18,19,20]
])

b_1 = np.array([21,22,23,24,25])
c = np.append(a,[b_1],axis=0)
print(c)

b_2 = np.array([21,22,23,24])
d = np.append(a,b_2.reshape(4,-1),axis=1)
print(d)

system('clear')

# 99 Insert rows/columns in Numpy

a = np.array([
  [ 1, 2, 3, 4, 5],
  [ 6, 7, 8, 9,10],
  [11,12,13,14,15],
  [16,17,18,19,20]
])
b = np.array([21,22,23,24,25])
c = np.insert(a,2,b,axis=0)
print(c)

b_2 = np.array([21,22,23,24])
d = np.insert(a,2,b_2,axis=1)
print(d)

system('clear')

# 100 Array Manipulation

a = np.array([
  [ 1, 2, 3, 4, 5],
  [ 6, 7, 8, 9,10],
  [11,12,13,14,15],
  [16,17,18,19,20]
])

b = np.delete(a,2,axis=0)
print(b)
c = np.delete(a,3,axis=1)
print(c)
