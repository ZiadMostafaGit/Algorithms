arr = [17, 5, -21, 15]
n = len(arr)
target = 14

def tryall(sum, i):
    if i == n:
        return sum % target == 0

    if tryall(sum=sum + arr[i], i=i + 1) or tryall(sum=sum - arr[i], i=i + 1):
        return 1

    return 0

print(tryall(0, 0))
