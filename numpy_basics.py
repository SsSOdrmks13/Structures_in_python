# # Applications of numpy
# # 1. Mathematics (MATLAB replacement)
# # 2. Plotting (Matplotlib python)
# # 3. Backend (Pandas, connect 4, Digital photography)
# # 4. Machine learning
#
# import numpy as np
# a = np.array([1, 2, 3], dtype='int32')
# print(a)
#
# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)
#
# # Get dimension
# x = a.ndim
# y = b.ndim
# print(x, y)
# # Get shape
# m = a.shape
# n = b.shape
# print(m, n)
# # Get type
# print(a.dtype, b.dtype)
# # Get size --> size of each item in numpy
# print(a.itemsize, b.itemsize)
# # Get total size
# print(a.size*a.itemsize, b.size*b.itemsize)
import numpy as np

# import numpy as np
#
# a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a.shape)
#
# # Accessing an element
# item = a[1][5]
# print(item)
#
# print(a[0, :])
# print(a[:, 0:2]) # all the rows, but 0 to 2 columns
#
# # Mutability
# a[1][3] = 45
# print(a)
# a[:, 4] = [99, 98] # change 4rth index of every row, to 98 and 99 repectively
# print(a)



# 3D array
# a = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
# print(a)
# print(a[0, 1, 1])
# print(a[0, 1, :])
# print(a[:, 0, :])


# # All zeroes matrix
# a = np.zeros((2, 3, 3))
# print(a)
# # All ones matrix
# b = np.ones((2, 3))
# print(b)
# # Any other number
# c = np.full((2,2), 99)
# print(c)
# # Any other number (full like)
# d = np.full_like(b, 4)
# print(d)

# # Random decimal numbers
# a = np.random.rand(4, 2)
# print(a)
# b = np.random.random_sample(a.shape)
# print(b)
# c = np.random.randint(7, 13, size=(3, 3))
# print(c)
# d = np.identity(3)  # identity matrix
# print(d)


# Repeat an array
a = np.array([[1, 2, 3]])
r1 = np.repeat(a, 3)
print(r1)





