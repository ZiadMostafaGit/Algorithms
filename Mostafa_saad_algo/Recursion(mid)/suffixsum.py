def suffixsum(arr, n, index):
    if index<len(arr)-n:
        return 0
    
    return arr[index] + suffixsum(arr, n, index=index-1)

arr = [1, 555, 3, 22, 6, 88, 555, 32, 511, 2, 21]
print(suffixsum(arr, 6, len(arr)-1))
