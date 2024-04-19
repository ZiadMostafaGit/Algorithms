def leftmax(arr,pos,maxval,index):
    if index<0:
        return 
    if index>=pos and arr[index]>maxval:
        maxval=arr[index]
    elif index<pos:
            arr[index]=maxval

    leftmax(arr,pos,maxval,index=index-1)
    return arr




arr=[1,555,3,22,6,88,555,32,511,2,21]
print(leftmax(arr,9,0,len(arr)-1))