def sum_with_index(arr, index):
    if index==len(arr):
        return
    arr[index]+=arr[index-1]
    sum_with_index(arr,index=index+1)


    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_with_index(arr,1)
print(result)
