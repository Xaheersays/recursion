arr= [2,1,4,5,0]

def Check(arr,i,n):
    if i==n:
        return True
    return arr[i] <= arr[i+1] and Check(arr,i+1,n)

print(Check(arr,0,len(arr)-1))