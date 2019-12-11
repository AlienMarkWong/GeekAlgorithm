# The ideas copied from LeetCode

def removeDuplicates(nums):
    flag = 0                  
    for num in nums:          
        if nums[flag] != num: 
            flag += 1         
            nums[flag] = num  
    return len(nums) and flag + 1


if __name__ == '__main__':
    a = [1, 1, 2]
    rs = removeDuplicates(a)
    print(rs)
