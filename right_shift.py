arr = [1,2,3,4,5,6,7,8]
pos = 4
print("Before Shift")
print(arr)
for i in range(len(arr)-1,pos-1,-1):
    arr[i] = arr[i-pos]
for i in range(0,pos):
    arr[i] = 0
    
# for i in range()
print("After Shift")
print(arr)