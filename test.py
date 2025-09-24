def counting(nums):
    counter={}
    for i in range(len(nums)):
        if nums[i] not in counter:
            counter[nums[i]] = 1
        else:
            counter[nums[i]] += 1
    return counter


nums=[1,1,2,3,4,5,6,7,7,7]

print(counting(nums))
