import time

def maxprod_no_dp(i, rem):
    if i == k:
        if rem == 0:
            return 1
        else:
            return float('-inf')

    if rem == 0:
        return 0

    ret = float('-inf')
    for j in range(1, rem + 1):
        res = maxprod_no_dp(i=i + 1, rem=rem - j) * j
        ret = max(ret, res)

    return ret

def maxprod_dp(i, rem, memo):
    if i == k:
        if rem == 0:
            return 1
        else:
            return float('-inf')

    if rem == 0:
        return 0

    if memo[i][rem] != -1:
        return memo[i][rem]

    ret = float('-inf')
    for j in range(1, rem + 1):
        res = maxprod_dp(i=i + 1, rem=rem - j, memo=memo) * j
        ret = max(ret, res)

    memo[i][rem] = ret
    return ret

# Testing without DP
def test_no_dp(s, k):
    start_time = time.time()
    result = maxprod_no_dp(0, s)
    end_time = time.time()
    print("Testing without dynamic programming:")
    print("Maximal product:", result)
    print("Time taken:", end_time - start_time, "seconds")

# Testing with DP
def test_with_dp(s, k):
    start_time = time.time()
    memo = [[-1] * (s + 1) for _ in range(k + 1)]
    result = maxprod_dp(0, s, memo)
    end_time = time.time()
    print("Testing with dynamic programming:")
    print("Maximal product:", result)
    print("Time taken:", end_time - start_time, "seconds")

# Test the difference
s = 50
k = 6

test_no_dp(s, k)
print()
test_with_dp(s, k)
