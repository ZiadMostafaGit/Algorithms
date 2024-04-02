

def arraymax(arr,index):
    if index==len(arr)-1:
        return arr[index]
    
    return max(arr[index],arraymax(arr,index=index+1))




arr=[1,555,3,22,6,88,555,32,511,2,21]
print(arraymax(arr,0))
