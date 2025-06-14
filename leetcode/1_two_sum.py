from typing import List

''' project description
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

'''
twoSum is O(n) -> traverse through array only once, insertion is O(1) [optimal]
twoSum_On2 is O(n2) -> traverse through nested loops
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary to store index, number
        num_map = {}

        # traverse index for each value
        for i, num in enumerate(nums):
            # complement is the next number needed to fulfill the target
            complement = target - num

            # check num_map for the value in complement
            if complement in num_map:
                '''
                    if true, then those 2 numbers get the sum
                    num_map[complement] -> index of complement
                    i -> index of current number in iteration
                '''
                return [num_map[complement], i]
            
            # no complement found means add the current num and its index to the num_map
            num_map[num] = i

        # returns blank if no 2 numbers equal the targets
        return []
    
    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # Outer loop: iterate through each number
        for i in range(n):
            # Inner loop: iterate through numbers *after* the current one
            # to find a pair. This ensures we don't use the same element twice
            # and avoid redundant pairs (e.g., (2,7) vs (7,2)).
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        # According to problem constraints, a solution always exists,
        # so this part should not be reached.
        return []

solver = Solution()

# 2 + 7 = 9 so index 0 and index 1 is [0,1]
nums_arg = [2, 7, 11, 15]
target_arg = 9
result = solver.twoSum(nums=nums_arg, target=target_arg)
print(result) 

result2 = solver.twoSum([3, 2, 4], 6)
print(result2)

result3 = solver.twoSum([3, 3], 6)
print(result3)

result3 = solver.twoSum([3, 3], 10)
print(result3) # returns [] since no 2 numbers sum to 10

result4 = solver.twoSum_On2([3,3], 6)
print(result4)