#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   December 30th, 2025

    LeetCode: #3 Longest Substring Without Repeating Characters

    Given a string s, 
    find the length of the longest substring w/o duplicate characters

    Constraints:
        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces

    Example 1:
        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3. 
                     Note that "bca" and "cab" are also correct answers
        
    Example 2:
        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1

    Example 3:
        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
                     Notice that the answer must be a substring, 
                     "pwke" is a subsequence and not a substring
        
    Usage:
        python3 main.py

    Solution:
        Accepted - 988 / 988 testcases passed

    Notes:
        TIME AND SPACE COMPLEXITY: Brute Force Approach
        -----------------------------------------------
        Metric           | Complexity | Reason
        -----------------------------------------------
        Time Complexity  | O(n^2)     | Nested loops: Inner loop runs up to n times for every outer loop step.
        Space Complexity | O(min(n,m))| Set stores at most n chars or size of alphabet (m).
        -----------------------------------------------
        

*********************************************************
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Calculates the length of longest substring w/o duplicate characters

        Args:
            s: input string of characters

        Returns:
            max_count: the length of the longest substring of unique sequential characters
        """
        characters = set()
        max_count = 0
        cur_count = 0

        for i in range(len(s)):
            for c in s[i:]:
                # Letter already exists in the dictionary, so will reset the set
                if c in characters:
                    if cur_count > max_count:
                        max_count = cur_count
                    characters.clear()
                    cur_count = 0
                    break
                # Letter is not yet in the dictionary, so will add to the set
                else:
                    characters.add(c)
                    cur_count += 1
            max_count = max(max_count, cur_count)
        
        return max_count

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
