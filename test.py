def test(nums,target):
    for i in range(len(nums)):
        slicednums=nums[i + 1:len(nums)]
        for j in range(len(slicednums)):
            if (nums[i] + slicednums[j] == target):
                return i, j

nums=[2,7,11,15]
target=9
t=test(nums,target)
print(t)