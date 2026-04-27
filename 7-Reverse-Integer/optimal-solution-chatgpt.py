#!/usr/bin/env python3
"""
********************************************************
    Author: ChatGPT + CBOMBS
    Date:   April 25th, 2026

    LeetCode: #7 Reverse Integer (*better)

    Problem:
    Given a signed 32-bit integer x, return x with its
    digits reversed.

    If reversed integer overflows signed 32-bit range:
        [-2^31, 2^31 - 1]
    return 0.

    ----------------------------------------------------
    Time & Space Complexity
    ----------------------------------------------------
    Let d = number of digits in x

    Time Complexity:
        O(d)
        - Process each digit once

    Space Complexity:
        O(1)
        - Uses only integer variables
        - No strings / arrays used

    ----------------------------------------------------
    Why This Is Optimal:
    - Uses math instead of string conversion
    - Checks overflow BEFORE it happens
    - Constant extra memory
*********************************************************
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        result = 0

        # Process digits until x becomes 0
        while x != 0:

            # Set to the right most digit
            digit = int(x % 10)

            # Remove the right most digit
            x = int(x / 10)

            # Overflow check BEFORE multiplying by 10
            if result > INT_MAX // 10 or (
                result == INT_MAX // 10 and digit > 7
            ):
                return 0

            if result < INT_MIN // 10 or (
                result == INT_MIN // 10 and digit < -8
            ):
                return 0

            # Build result by shifting left one decimal place 
            # and add digit on the right
            result = result * 10 + digit

        return result


if __name__ == "__main__":
    x1 = 321
    x2 = 1534236469

    sol = Solution()
    print(sol.reverse(x2))   # 0 (overflow)