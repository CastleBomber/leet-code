#!/usr/bin/env python3
''' 
    LeetCode
    Koni's Optimal Solution

    TIME AND SPACE COMPLEXITY: Sliding Window with Deque
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Each char is added/removed from deque at most once.
    Space Complexity | O(min(n,m))| Deque size depends on string (n) or alphabet (m).
    ----------------------------------------------------

    TIME COMPLEXITY COMPARISON: List vs. Deque
    ------------------------------------------
    Feature                | List         | Deque
    ------------------------------------------
    Access Middle Elements | O(1) (Fast)  | O(n) (Slow)
    Add/Remove at End      | O(1)         | O(1)
    Add/Remove at Start    | O(n) (Slow)  | O(1) (Fast)
    ------------------------------------------
'''
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0     # result
        q = deque() # "deck", double-ended queue
        for c in s:
            if c in q:
                while q.popleft() != c:
                    pass
            q.append(c)
            res = max(res, len(q))
        
        return res
    
if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = " "
    s5 = "dvdf"
    s6 = "asjrgapa"
    s7 = "jbpnbwwd"

    sol = Solution()
    result = sol.lengthOfLongestSubstring(s7)

    print(result)