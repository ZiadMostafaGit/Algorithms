def suffixsum(arr, n, index):
    if index + n > len(arr):
        return 0 
    if index == len(arr) - 1:
        return arr[index]
    return arr[index] + suffixsum(arr, n, index + 1)

arr = [1, 555, 3, 22, 6, 88, 555, 32, 511, 2, 21]
print(suffixsum(arr, 4, 0))
