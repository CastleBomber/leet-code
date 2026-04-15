#!/usr/bin/env python3
"""
********************************************************
    Author: Deepseek + CBombs
    Date:   March 8th, 2026
    Purpose: Prepping for IBM coding test

    LeetCode: #1446 Consecutive Characters

    The power of the string is the maximum length of a non-empty substring 
    that contains only one unique character.

    Given a string s, return the power of s.

    Example 1:
        Input: s = "leetcode"
        Output: 2
        Explanation: The substring "ee" is of length 2 with the character 'e' only.

    Example 2:
        Input: s = "abbcccddddeeeeedcba"
        Output: 5
        Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

    Constraints:
        1 <= s.length <= 500
        s consists of only lowercase English letters.

    Usage:
        python3 optimal-solution-deepseek.py

    Notes:
    
    TIME AND SPACE COMPLEXITY: Single Pass Scan
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Single loop through the string of length n.
                                    Each character is examined once; operations are constant-time.
    Space Complexity | O(1)       | Only a fixed number of integer variables (max_power, curr_count)
                                    and one character variable (prev) are used.
                                    No additional data structures depend on input size.
    ----------------------------------------------------
*********************************************************
"""

class Solution:
    def maxPower(self, s: str) -> int:
        # Edge case: empty string (not needed per constaints, but safe)
        if not s:
            return 0
        
        max_power = 1   # At least 1 for non-empty string
        curr_count = 1  # Length of current run of identical characters
        prev = s[0]     # Previous character

        # Start from the second character (index 1)
        for i in range(1, len(s)):
            curr = s[i]
            if curr == prev:
                # Same as previous, extend current run
                curr_count += 1
                # Update max_power if needed
                if curr_count > max_power:
                    max_power = curr_count
            else:
                # Different character, start a new run
                prev = curr
                curr_count = 1

        return max_power
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["leetcode", "abbcccddddeeeeedcba", "tourist", "cc"]
    for s in test_cases:
        print(f"maxPower('{s}') = {sol.maxPower(s)}")