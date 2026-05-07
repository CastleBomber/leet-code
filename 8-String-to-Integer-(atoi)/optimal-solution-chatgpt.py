#!/usr/bin/env python3
"""
********************************************************
    Author: ChatGPT + CBOMBS
    Date:   April 25th, 2026

    LeetCode: #8 String to Integer (atoi)

    Convert a string into a 32-bit signed integer.

    Rules:
    1. Ignore leading spaces
    2. Optional '+' or '-'
    3. Read digits until non-digit
    4. If no digits found -> 0
    5. Clamp to 32-bit signed range:
       [-2147483648, 2147483647]

    TIME AND SPACE COMPLEXITY: Single‑Pass with Overflow Prevention
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Scan string once
    |
    Space Complexity | O(1)       | Only a few variables used


********************************************************
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # ------------------------------------------------
        # 1. Skip leading spaces
        # ------------------------------------------------
        while i < n and s[i] == " ":
            i += 1

        # If string was only spaces
        if i == n:
            return 0

        # ------------------------------------------------
        # 2. Check sign
        # ------------------------------------------------
        sign = 1

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        # ------------------------------------------------
        # 3. Build number from digits
        # ------------------------------------------------
        num = 0

        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Overflow check BEFORE adding digit
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        # ------------------------------------------------
        # 4. Apply sign
        # ------------------------------------------------
        return sign * num


if __name__ == "__main__":
    sol = Solution()

    # Test 1: normal positive
    #print(sol.myAtoi("42"))              # 42

    # Test 2: leading spaces + negative + zeros
    #print(sol.myAtoi("   -042"))        # -42

    # Test 3: overflow case
    print(sol.myAtoi("91283472332"))    # 2147483647