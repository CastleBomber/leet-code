#!/usr/bin/env python3
''' 
    LeetCode: #3 Longest Substring Without Repeating Characters (Best)
    Authors: Rahul Varma's Optimal Solution + CBombs (edits)

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

    TIME AND SPACE COMPLEXITY: Two-Pointer Sliding Window
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Each pointer (left/right) moves at most n times.
    Space Complexity | O(min(n,m))| Set stores at most n chars or size of alphabet (m).
    ----------------------------------------------------

    Notes:
        Set vs List
        Able to use set here since uniqeness is similar to 'non-duplicate characters'
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLength = 0
        left = 0 # Stays more on the left and moves forward to the right
        
        # Moves to the right
        for right in range(len(s)):
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