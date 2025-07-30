def linear_search(arr,find):
    for i in range(len(arr)):
        if arr[i]==find:
            return i
arr = [434,43,55,66,77,788,99,100]
find = 66
index = linear_search(arr, find)
print("Element found at index:", index) if index is not None else print("Element not found")