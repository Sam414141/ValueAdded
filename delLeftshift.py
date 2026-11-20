# arr = [5,10,15,20,25,30]
# pos = 2
# for i in range(pos,len(arr)-1):
#     arr[i] = arr[i+1]
# arr[len(arr)-1] = 0
# print(arr)


nums = [0,1,0,3,12]
i = 0
for j in range(0,len(nums)):
    if nums[j] != 0:
        nums[j],nums[i] = nums[i],nums[j]
        # nums[i] = nums[j]
        i += 1
        
print(nums)