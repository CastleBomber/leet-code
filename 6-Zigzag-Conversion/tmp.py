#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 4th, 2026

    LeetCode: #6 Zigzag Conversion

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
    (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
    

    Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"

    Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        
        P     I    N
        A   L S  I G
        Y A   H R
        P     I

    Example 3:
        Input: s = "A", numRows = 1
        Output: "A"
    

    Constraints:
        1 <= s.length <= 1000
        s consists of English letters (lower-case and upper-case), ',' and '.'.
        1 <= numRows <= 1000

    Usage:
        python3 tmp.py

    Solution:
    

    Notes:

*********************************************************
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        @param s: Input string consisting of English letters, ",", and "."
        @param numRows: the number of rows in the zigzag pattern
        @return: string as read, line by line
        """
        input = list(s)
        output = list()
        cur_row = 0
        bigJump = numRows + (numRows - 2)
        output.append(input[0])

        while (cur_row < numRows) and (bigJump < len(input)):
            if cur_row == 0:
                # Add to output
                output.append(input[bigJump])

                # Remove from input list
                input.pop(input[bigJump])
            else:
                output.append(input[bigJump])
                output.append(input[bigJump+1])
            
            bigJump = bigJump - 2


        return output


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3

    sol = Solution()
    result = sol.convert(s, numRows)

    print(result)
