arr= [2,1,4,5,0,9]


def Attendence(arr,n,i,target):
    if i == n:
        return False
    return arr[i]==target or Attendence(arr,n,i+1,target)

# print(Attendence(arr,len(arr),0,3))


arr= [2,1,4,5,0,9,9,9]


def AttendenceL(arr,n,i,target,l):
    if i == n:
        return l
    if arr[i] == target :
        l.append(i)
    return AttendenceL(arr,n,i+1,target,l)
print(AttendenceL(arr,len(arr),0,9,[]))
