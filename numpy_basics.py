import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(arr1)
print(arr2)
print(arr2.shape)
print(arr2.ndim)
print(arr2.size)
print(arr2.dtype)
a = np.array([10,20,30])
b = np.array([1,2,3])

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.std(a))

print(arr1[0])
print(arr1[2])
print(arr1[1:4])

numbers = np.array([1,2,3,4,5,6])

print(numbers.reshape(2,3))

print(np.zeros((3,3)))
print(np.ones((2,4)))
print(np.arange(1,11))
print(np.linspace(0,10,5))