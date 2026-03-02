#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS + ChatGPT
    Date:   January 10th, 2026

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

    Usage:
        python3 main.py

    Solution:
        Accepted - 143 / 143 test cases passed
        Runtime: 219 ms  (Beats 88.77%)
        Memory: 19.16 MB (Beats 90.87%)

        
    TIME AND SPACE COMPLEXITY: Center Expansion
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n²)      | For each index (n centers), expansion
                                    may scan outward up to n characters.
                                    Worst case: "aaaaaa..."
    Space Complexity | O(1)       | Only uses a few integer pointers.
                                    No extra data structures.
    ----------------------------------------------------


    Notes:

*********************************************************
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring using center expansion

        @param s: Input string consisting of English letters
        @return: Longest palindromic substring in s
        """
        start = 0
        end = 0     # end - start = length of palindrome

        # Iterate through each index treating it as a potential palindrome center
        for i in range(len(s)):
            l1, r1 = self.expand(s, i, i)    # Case 1: Odd-length palindrome (single character center)
            l2, r2 = self.expand(s, i, i+1)  # Case 2: Even-length palindrome (center b/n two characters)

            # Update longest palindrome if odd-length result is larger
            if r1 - l1 > end - start:
                start, end = l1, r1

            # Update longest palindrome if even-length result is larger
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]

    def expand(self, s, left, right):
        """
        Expands outward from the given left and right indices
        while the substring remains a palindrom
        Ex:
            [a   *b*   a]
            [a   *b* *b*   a]

        @param s: Input string
        @param left: Left pointer (starting center position)
        @param right: Right pointer (odd check: center, even check: center + 1)
        @return: Tuple (start_index, end_index) of the largest valid palindrom
                 found from this center
        """
        # Expand as long as boundaries are valid and characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        # Loop exits one step beyond valid palindrome -> adjust back
        return left+1, right-1

if __name__ == "__main__":
    # s = "babad"
    # s = "aacabdkacaa"
    # s = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    s = "abbad"

    sol = Solution()
    result = sol.longestPalindrome(s)

    print(result)
