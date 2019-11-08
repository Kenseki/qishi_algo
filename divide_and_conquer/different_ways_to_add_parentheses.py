# Time: O(NlogN)?
# Space: O(N)？


# Runtime: 28 ms, faster than 99.72% of Python3 online submissions for Different Ways to Add Parentheses.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Different Ways to Add Parentheses.
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
        def aux(input):
            if input.isdigit():
                return [int(input)]
        
            ans = []
            for i in range(len(input)):
                if input[i] in ['+', '-', '*']:
                    left = aux(input[:i])
                    right = aux(input[i+1:])
                
                    ans += [ops[input[i]](num1, num2) for num1 in left for num2 in right]
            return ans
        
        if not input:
            return []
        
        return aux(input)
                