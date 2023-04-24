# Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one 
# solution, and you may not use the same element twice.

# You can return the answer in any order.

##### Example 1 ########

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    
"""
    
##### Example 2 ########

"""
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""
    
##### Example 3 ########

"""
Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Plan: Brute Force
        
        # loop through the list with 2 index pointers
        # have first point on the first element and have the second point to
        # the next element
        
        # each time the second pointer move compare the sum of the first element
        # and the second element to the target number if its the same return
        # both index numbers
        
        # if the second element don't match, have the second pointer to iterate till
        # the end of the list
        
        # the first iterator will point to the next element and the second iterator will
        # point to the next element right after the second element
        
        # rinse and repeat
        
        # for i, a in enumerate(nums, start=0):
        #     for j, b in enumerate(nums[i+1:], start=0):
        #         # print(f"{a},{b}")
        #         if a+b == target:
        #             return(i, j+i+1)
        
        # time and space n^2
        #----------------------------------------------------------
        # Plan: using BST
        
        # list have to be sorted
        # have 2 pointers, one pointing to the lowest number the other
        # pointing to highest number
        # lowest pointer will move to the right each time the sum
        # of the two pointer is less than the target
        # if the sum gets over target, the highest pointer will move to the left
        # this will occur till target match or not
        
        # Bad part since the original list was sorted we lost the original index
        # ----------------------------------------------------------------
        
        # Plan: using Hashmap
        
        # possible_number = target - nums[index] (Math game)
        # the idea is that will keep storing the possible numbers we see and it's index
        # in the hashmap if we come accross the existing number that means
        # we have the previous index and the current index were pointing
        checker= {}
        
        for index in range(len(nums)):
            diff = target - nums[index]
            if diff in checker:
                return [checker[diff], index]
            else:
                checker[nums[index]] = index
                
        
    
test = Solution()
nums1 = [2,11,7,15]
target1 = 9

nums2 = [3,2,4]
target2 = 6

nums3 = [3,3]
target3 = 6

ans1 = test.twoSum(nums1, target1)
print(ans1)

ans2 = test.twoSum(nums2, target2)
print(ans2) 

ans3 = test.twoSum(nums3, target3)
print(ans3) 