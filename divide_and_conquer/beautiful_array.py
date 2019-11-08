# DP

# Time: O(N^2) is it possible to reduce?
# Space: O(N^2)

# Runtime: 232 ms, faster than 9.32% of Python3 online submissions for Beautiful Array.
# Memory Usage: 25.3 MB, less than 50.00% of Python3 online submissions for Beautiful Array

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1:[1]}
        for i in range(2, N+1):
            odds = memo[(i+1)//2]
            evens = memo[i//2]
            
            memo[i] = [2*x-1 for x in odds]+[2*x for x in evens]
        
        return memo[N]

# Divide and conquer

# Time: O(NlogN)
# Space: O(NlogN)

# Runtime: 28 ms, faster than 99.58% of Python3 online submissions for Beautiful Array.
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Beautiful Array.
class Solution:
    def beautifulArray(self, N):
        memo = {1: [1]}
        def f(N):
            if N not in memo:
                odds = f((N+1)//2)
                evens = f(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        return f(N)