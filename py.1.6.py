def count(nums):
    count_dict={}
    for num in nums:
        if num in count_dict:
            count_dict[num] +=1
        else:
            count_dict[num] = 1
    return count_dict
nums = [1,2,3,4,1,2,3]
t=count(nums)
print(t)
