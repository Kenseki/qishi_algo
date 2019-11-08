# Binary search

# Time: O(logN)
# Space: O(logN)

# Runtime: 48 ms, faster than 99.57% of Python3 online submissions for Search Insert Position.
# Memory Usage: 13.6 MB, less than 83.58% of Python3 online submissions for Search Insert Position.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarySearch(nums, target, start, end):
            
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            
            if start >= end:
                
                if target > nums[start]:
                    return start + 1
                else:
                    return start
            
            if target > nums[mid]:
                return binarySearch(nums, target, mid+1, end)
            else:
                return binarySearch(nums, target, start, mid-1)
        
        if not nums:
                return 0
        return binarySearch(nums, target, 0, len(nums)-1)