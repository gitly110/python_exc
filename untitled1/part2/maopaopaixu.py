nums=[3,1,25,10,15,6,8]
for i in range(len(nums)-1):
    for j in range(len(nums)-1-i):
        if nums[j]<nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            print(nums)
x=7
for k in nums:
    if x>k:
        print(nums.index(k))
        break
nums.insert(nums.index(k),x)
print(nums)



