# Binary search

# Time: O(logN)
# Space: O(logN) (recursoin stack)

# Runtime: 36 ms, faster than 99.72% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 13.2 MB, less than 76.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binarySearch(nums, start, end):
            if start == end:
                return nums[start]
            
            mid = (start+end)//2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                return binarySearch(nums, mid+1, end)
            else:
                return binarySearch(nums, start, mid)
        
        if not nums:
            return None
        elif len(nums) == 1 or nums[0]<nums[-1]:
            return nums[0]

        return binarySearch(nums, 0, len(nums)-1)
                