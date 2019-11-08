# Quicksort

# Time: O(N) because we only need to deal with one half of the array iteration
# Space: O(1) this is in-place sort.

# Runtime: 108 ms, faster than 24.18% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.

class Solution:
    def kthSmallest(self, k, nums):
        def partition(nums, start, end):
            mid = (start+end)//2

            if nums[start] >nums[mid]:
                nums[start], nums[mid] = nums[mid], nums[start]
            if nums[start] > nums[end]:
                nums[start], nums[end] = nums[end], nums[start]
            if nums[mid] > nums[end]:
                nums[mid], nums[end] = nums[end], nums[mid]

            nums[mid], nums[end] = nums[end], nums[mid]

            pivot = nums[end]
            print('pivot:', nums[end])
            i = start
            j = end -1

            while i<=j:
                if nums[i] <= pivot:
                    i+=1
                    continue
                if nums[j] > pivot:
                    j-=1
                    continue

                nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j-=1
            print(nums)
            nums[i], nums[end] = nums[end], nums[i]
            print(nums)
            return i

        if k > len(nums):
            return None
        if not nums:
            return None

        start = 0
        end = len(nums)-1
        pivot_index = partition(nums, start, end)

        while pivot_index != k-1:
            print(pivot_index)
            if pivot_index < k:
                start = pivot_index+1
                pivot_index = partition(nums, start, end)
            else:
                end = pivot_index-1
                pivot_index = partition(nums, start, end)

        return nums[pivot_index]