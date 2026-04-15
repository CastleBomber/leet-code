#!/usr/bin/env python3
"""
********************************************************
    Author: Deepseek + CBOMBS
    Date:   March 26th, 2026

    LeetCode: #6 Zigzag Conversion

    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
    of rows like this:

    P   A   H   N
    A P L S I I G
    Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"

    Write the code that will take a string and make this conversion given a
    number of rows.

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
        s consists of English letters (lower-case and upper-case), ',' and '.'
        1 <= numRows <= 1000

    Usage:
        python3 optimal-solution-deepseek.py

    Solution:
        Simulation using a list of strings to collect characters per row.

    TIME AND SPACE COMPLEXITY: Simulation with Row Strings
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | We traverse the input string once, where n is the
                                    length of the string. Each character is processed
                                    in constant time.
    Space Complexity | O(n)       | The rows list stores all characters across the
                                    rows. In the worst case, we store the entire
                                    string in the rows list, so space is O(n).
    
*********************************************************
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string into a zigzag pattern and read it row by row.

        Args:
            s: Input string consisting of English letters, "," and "."
            numRows: Number of rows in the zigzag pattern

        Returns:
            The converted string read row by row.
        """
        # Edge case: if there's only one row, no zigzag is formed
        if numRows == 1:
            return s

        # Create a list of empty strings for each row
        # Use min(numRows, len(s)) to avoid creating more rows than characters
        rows = ['' for _ in range(min(numRows, len(s)))]

        current_row = 0          # Current row we are filling
        going_down = False       # Direction flag: True if moving down, False if moving up

        # Traverse each character in the input string.
        for char in s:
            rows[current_row] += char   # Append character to its row

            # If we are at the top row (0) or the bottom row (numRows-1),
            # reverse the direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            # Move to the next row: down if going_down, otherwise up
            current_row += 1 if going_down else -1

        # Combine all rows into a single result string.
        return ''.join(rows)


if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Provided example.
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = sol.convert(s1, numRows1)
    print(f'Input: s = "{s1}", numRows = {numRows1}')
    print(f'Output: "{result1}"')          # Expected: "PAHNAPLSIIGYIR"
    print()

    # Test case 2: Provided example with 4 rows.
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    result2 = sol.convert(s2, numRows2)
    print(f'Input: s = "{s2}", numRows = {numRows2}')
    print(f'Output: "{result2}"')          # Expected: "PINALSIGYAHRPI"
    print()

    # Test case 3: Single character.
    s3 = "A"
    numRows3 = 1
    result3 = sol.convert(s3, numRows3)
    print(f'Input: s = "{s3}", numRows = {numRows3}')
    print(f'Output: "{result3}"')          # Expected: "A"
    print()

    # Additional test cases:
    # # Test case 4: numRows >= len(s) (no zigzag, just vertical).
    # s4 = "HELLO"
    # numRows4 = 10
    # result4 = sol.convert(s4, numRows4)
    # print(f'Input: s = "{s4}", numRows = {numRows4}')
    # print(f'Output: "{result4}"')        # Expected: "HELLO"
    #
    # # Test case 5: Empty string (should return empty).
    # s5 = ""
    # numRows5 = 3
    # result5 = sol.convert(s5, numRows5)
    # print(f'Input: s = "{s5}", numRows = {numRows5}')
    # print(f'Output: "{result5}"')        # Expected: ""
    #
    # # Test case 6: All rows filled.
    # s6 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # numRows6 = 5
    # result6 = sol.convert(s6, numRows6)
    # print(f'Input: s = "{s6}", numRows = {numRows6}')
    # print(f'Output: "{result6}"')