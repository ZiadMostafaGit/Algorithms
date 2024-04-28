arr = [[5, 1, 2], [6, 7, 8], [1, 4, 9]]
dp = [[-1 for _ in range(3)] for _ in range(3)]

def is_valid(r, c):
    return 0 <= r < len(arr) and 0 <= c < len(arr[0])

def maxpathsum(r, c):
    if not is_valid(r, c):
        return 0

    if dp[r][c] != -1:
        return dp[r][c]

    right_path = maxpathsum(r, c + 1)
    down_path = maxpathsum(r + 1, c)

    dp[r][c] = arr[r][c] + max(right_path, down_path)
    return dp[r][c]

print(maxpathsum(0, 0))