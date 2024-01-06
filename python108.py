# Numpy - a muti dimntional array library, fast compared to lists cus it take less memory and no type checjing when itterting 
import numpy as np
# intialize an array
a = np.array([1,2,3], dtype='int16') # 1 dimentional list, with data type specified
b = np.array([[1,2,3],[4,5,6]]) # 2d list with a list
print(b)
# to get the number of dimetions 
print(b.ndim)
# to get the shape (rows, columns)
print(b.shape)
# to get the data type
print(a.dtype)
# to get the byte size, note: 1 byte or itemsize = int8, 00000000
print(a.itemsize)
#Accessing and changing specific elements, [row,column] which index based i.e. start at 0, we can use -ve to access from the back
print(b[1,2])
# to access only the row or the column
print(b[0,:]) #the 1st row
print(b[:,1]) #the 2nd column
# to change it just set the accessed value to a value
b[1,1] = 55 # to change a specific value
b[:,1] = 9 # to change the whole column with same value
b[1,:] = [85,22,19] # to change the whole row with specified values
print(b)
# 3d
d = np.array([[[a,b,c],[d,e,f]],[[g,h,i],[j,k,l]]]) 
print(d.shape)
# to access an element
print(d[0,0,1])


