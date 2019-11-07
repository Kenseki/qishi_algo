# divide and conquer

# Runtime: 156 ms, faster than 5.17% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.7 MB, less than 52.03% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_into_three(nums, start, end):
            if start == end:
                return nums[start]
            
            mid = (start + end)//2
            
            left_sum = divide_into_three(nums, start, mid)
            right_sum = divide_into_three(nums, mid+1, end)
            
            mid_sum = 0
            mid_left_sum = float('-inf')
            mid_right_sum = float('-inf')
            
            current_sum = 0
            for i in range(mid, start-1, -1):
                current_sum += nums[i]
                mid_left_sum = max(mid_left_sum, current_sum)
            
            current_sum = 0
            for i in range(mid+1, end+1):
                current_sum += nums[i]
                mid_right_sum = max(mid_right_sum, current_sum)
            
            mid_sum = mid_left_sum + mid_right_sum
            
            return max(left_sum, right_sum, mid_sum)
        
        if not nums:
            return 0
        return divide_into_three(nums, 0, len(nums)-1)


# DP

# Time: O(N)
# Space: O(1)

# Runtime: 72 ms, faster than 93.33% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 13.6 MB, less than 64.23% of Python3 online submissions for Maximum Subarray.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
            max_sum = max(nums[i], max_sum)
        
        return max_sum
                
                