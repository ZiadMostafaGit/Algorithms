def sum_with_index(arr, length):
    if length == 0:
        return arr
    arr = sum_with_index(arr, length - 1)
    arr[length - 1] += length - 1
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_with_index(arr, len(arr))
print(result)
