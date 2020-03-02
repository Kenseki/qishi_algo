# binary search

# Time: O(NlogN)


# A: presorted array
# left, right: index of array
# x: target element

# Solution1: recursion
def binarySearch(A, left, right, x):
	if left >= right:
		return -1 # element not found

	mid = left + (right - left)//2 # do not use (left+right)//2 because (left+right) can exceed range of an integer

	if A[mid] == x:
		return mid
	elif A[mid] > x:
		return binarySearch(A, left, mid-1, x)
	else:
		return binarySearch(A, mid+1, right, x)

# Solution2: while loop
def binarySearch(A, x):
	N = len(A)

	if N == 0:
		return -1 # element not found
	if N == 1 and A[0] != x:
		return -1 # element not found

	left, right = 0, N-1

	while left < right:
		mid = left + (right - left)//2 # do not use (left+right)//2 because (left+right) can exceed range of an integer

		if A[mid] == x:
			return mid
		elif A[mid] > x:
			right = mid-1
		else:
			left = mid+1

	return -1











