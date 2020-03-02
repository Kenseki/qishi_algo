# Binary Search – Duplicated Elements
# Question: If the array to be searched was [1,2,3,3,4,4,4,5,5,5,5,5,6] and the target is 5
#           How to find the left most element or the right most element?

# Time: O(NlogN)

# A: presorted array
# x: target element
def duplicatedBinarySearch(A, x):
	N = len(A)

	if N == 0:
		return -1 # element not found
	if N == 1 and A[0] != x:
		return -1 # element not found

	left, right = 0, N-1

	while left < right:
		mid = left + (right - left)//2 # do not use (left+right)//2 because (left+right) can exceed range of an integer

		if A[mid] == x:
			# find leftmost
			while A[mid] == x:
				mid -= 1

			leftmost = mid+1
			return leftmost

			# finding rightmost will be similar
		elif A[mid] > x:
			right = mid-1
		else:
			left = mid+1

	return -1
