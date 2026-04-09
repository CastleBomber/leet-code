#!/usr/bin/env python3
''' 
    ChatGPT's Optimal Solution (best)
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
        if not s:
            return ""

        # Transform string to handle even-length palindromes
        # Example: "abba" -> "^#a#b#b#a#$"
        t = "^#" + "#".join(s) + "#$"
        n = len(t)

        P = [0] * n   # P[i] = palindrome radius centered at i
        center = 0
        right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            # Use mirror if inside current right boundary
            if i < right:
                P[i] = min(right - i, P[mirror])

            # Expand around center i
            while t[i + 1 + P[i]] == t[i - 1 - P[i]]:
                P[i] += 1

            # Update center and right boundary
            if i + P[i] > right:
                center = i
                right = i + P[i]

        # Find longest palindrome
        max_len = max(P)
        center_index = P.index(max_len)

        # Convert back to original string index
        start = (center_index - max_len) // 2

        return s[start:start + max_len]
    

if __name__ == "__main__":
    s = "abbad"

    sol = Solution()
    result = sol.longestPalindrome(s)

    print(result)

