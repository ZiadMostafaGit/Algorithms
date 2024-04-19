def ispalindrome(arr, left, right):
    if left >= right:
        return True
    
    if arr[left] != arr[right]:
        return False
    
    return ispalindrome(arr, left + 1, right - 1)

arr = [1, 5, 3, 1, 1, 3, 5, 1]
print(ispalindrome(arr, 0, len(arr) - 1))
