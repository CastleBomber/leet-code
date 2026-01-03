#!/usr/bin/env python3
''' 
    LeetCode
    Rahul Varma's Optimal Solution

    TIME AND SPACE COMPLEXITY: Two-Pointer Sliding Window
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Each pointer (left/right) moves at most n times.
    Space Complexity | O(min(n,m))| Set stores at most n chars or size of alphabet (m).
    ----------------------------------------------------
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0 # Stays more on the left and moves forward to the right
        
        # Moves to the right
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                # Remove all characters in charSet up to and including the original duplicate
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                # After some items removed, will continue with suitable substring
                charSet.add(s[right])
        
        return maxLength
    
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