def powerfunc(val,pow):
    if pow<=1:
        return val
    
    return val*powerfunc(val,pow-1)



print(powerfunc(5,5))