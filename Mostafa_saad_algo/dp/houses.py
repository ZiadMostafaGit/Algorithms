red = []
green = []
blue = []
oo = 10000000

n = int(input())

for i in range(n):
    string_input = input()
    values = string_input.split()  
    red.append(int(values[0]))  
    green.append(int(values[1]))  
    blue.append(int(values[2]))  

memo = [[None] * n for _ in range(5)]  

def minfunc(last, i):
    if i == n:
        return 0
    
    if memo[last][i] is not None: 
        return memo[last][i]
    
    rgb = oo
    
    if last != 0:
        rgb = min(rgb, red[i] + minfunc(0, i + 1))
    if last != 1:
        rgb = min(rgb, green[i] + minfunc(1, i + 1))
    if last != 2:
        rgb = min(rgb, blue[i] + minfunc(2, i + 1))

    memo[last][i] = rgb  # Memoize the result
    return rgb

print(minfunc(4, 0))
