arr = [5,10,15,20,25,30]
i = 0
for j in range(len(arr)):
    if arr[j] != 10:
        arr[i] = arr[j]
        i += 1

for j in range(i, len(arr)):
    arr[j] = 0

print(arr)