# given non-empty array of ints
# every element appears twice except one
# Example: input: [2,2,1]
# output: 1
# Example 2: input: [4, 1, 2, 1, 2]
# output: 4
def singleNumber(nums):
    nums.sort()
    while len(nums) > 1:
        if nums[0] == nums[1]:
            nums.pop(0)
            nums.pop(0)
        else:
            return nums[0]
    return nums[0]

my_input = [2,2,1]
print(singleNumber(my_input))
my_input2 = [4, 1, 2, 1, 2]
print(singleNumber(my_input2))
