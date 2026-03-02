#!/usr/bin/env python3
''' 
    Gourav Yadav's Optimal Solution
    Approach: Manacher's Algorithm

    LeetCode: #5 Longest Palindromic Substring
    
    Given a string s, return the longest palindromic substring in s

    Example 1:
    Input: s = "babad"
    Output: "bab"
    Optional: "aba" is also a valid answer

    Example 2:
    Input: s = "cbbd"
    Output: "bb"


    Constraints:
        1 <= s.length <= 1000
        s consist of only digits and English letters

        
    TIME AND SPACE COMPLEXITY: Manacher’s Algorithm
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Each character is processed once.
                                    Expansion work is reused via mirror logic.
                                    The right boundary only moves forward.
    Space Complexity | O(n)       | Uses transformed string (≈2n)
                                    and radius array P of size n.
    ----------------------------------------------------
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str

if __name__ == "__main__":
    s = "abbad"

    sol = Solution()
    result = sol.longestPalindrome(s)

    print(result)

