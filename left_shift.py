arr = [1,2,3,4,5,6,7,8]
pos = 3
print("Before Shift")
print(arr)
for i in range(0,len(arr)-pos):
    arr[i] = arr[i+pos]
    
# for i in range(len(arr)-1,(len(arr)-1)-pos,-1):
for i in range(len(arr)-pos,len(arr),1):
    arr[i] = 0
print("After Shift")
print(arr)