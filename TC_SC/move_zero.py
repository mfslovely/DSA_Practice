def sift_zero_lst(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] !=0:
            nums[non_zero_index],nums[i] = nums[i],nums[non_zero_index]
            non_zero_index +=1
    return nums

nums = [1,0,6,0,7]
print(sift_zero_lst(nums))



# another way

def move_zeros_to_end(arr):
    count = 0  

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr  

array = [0, 3, 0, 5, 0, 2, 0, 1]
print(move_zeros_to_end(array)) 

# another way
def move_zeros(arr):
    result = [num for num in arr if num != 0]
    zeros_count = arr.count(0)
    result.extend([0] * zeros_count)
    return result

array = [0, 4, 0, 2, 0, 5, 0]
print(move_zeros(array))