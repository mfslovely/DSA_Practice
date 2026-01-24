def sift_zero_lst(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] !=0:
            nums[non_zero_index],nums[i] = nums[i],nums[non_zero_index]
            non_zero_index +=1
    return nums

nums = [1,0,6,0,7]
print(sift_zero_lst(nums))