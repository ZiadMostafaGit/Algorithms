import time



def fibonacci_naive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

def fibonacci_list(n):
    dp = [-1] * (n+1)  
    
    def helper(n, dp):
        if n <= 1:
            dp[n] = n
            return dp[n]
        if dp[n] != -1:
            return dp[n]
        dp[n] = helper(n-1, dp) + helper(n-2, dp)
        return dp[n]
    
    return helper(n, dp)

def fibonacci_dict(n):
    dp = {}  
    
    def helper(n, dp):
        if n <= 1:
            return n
        if n in dp:
            return dp[n]
        dp[n] = helper(n-1, dp) + helper(n-2, dp)
        return dp[n]
    
    return helper(n, dp)

def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The {n}th Fibonacci number is: {result}")
    print(f"Time taken by {func.__name__}: {elapsed_time:.6f} seconds")

n = 35  

print("\nUsing a list for memoization:")
measure_time(fibonacci_list, n)
