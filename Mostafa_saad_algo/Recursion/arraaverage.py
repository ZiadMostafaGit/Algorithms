def arraysum(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    
    return arr[index] + arraysum(arr, index=index + 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arraysum(arr, 0) / len(arr))
