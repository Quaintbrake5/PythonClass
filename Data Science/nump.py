import numpy as np

arr = np.array([45]) # 0-D
arr = np.array([[1,2,3,4,5]]) # 1-D
arr = np.array([1,3,4] , [2,5,6]) # 2-D
arr = np.array([[[1,2,3], [4,5,6], [7,8,9]]]) # 3-D
# print(arr)

arr = np.array([1,2,3,4], ndmin=6)
# print (arr)
# print(arr.ndim)

arr = np.array([[1,2,3], [4,5,6]])
# print(arr[1],[1])
# print(arr[1,1])

fruits = np.array(["mango", "apple", "banana", "strawberry"])
# print(fruits.dtype)

arr = np.array([10,20,30,40,50])
# arr.astype('i')

arr = np.array([[1,2,3],[4,5,6],[10,20,30]])
# print(arr.size)
# print(arr.shape)

# print(arr[0,0]) #(row 0, column 0)

# print(np.random.rand(2,2)) # Generates random [2,2] matrix
# print(np.random.rand(2,1))

sales = np.array([
    [30, 50, 70], #day 1
    [10, 20, 30],
    [60, 50, 10],
])

print("Sales Data: ", sales)
print("Total per product: ", sales.sum(axis=0))

print("Average eggs sold: ", sales[::,2].mean())

days = [1,2,3,4,5]
sales = [10,20,30,40,50]