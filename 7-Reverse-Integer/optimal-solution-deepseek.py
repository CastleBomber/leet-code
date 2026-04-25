#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   April 25th, 2026

    LeetCode: #7 Reverse Integer

    Given a signed 32-bit integer x, return x with its digits reversed.
    If reversing x causes the value to go outside the
    signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers.

    Examples:
        Input: x = 123   -> Output: 321
        Input: x = -123  -> Output: -321
        Input: x = 120   -> Output: 21

    Constraints:
        -2^31 <= x <= 2^31 - 1

    Usage:
        python3 main.py

    Solution:
        Pop digits from the end using modulo 10, build result with overflow
        checks performed **before** multiplying/adding.

    Complexity:
        TIME    | O(n) where n = number of digits (max 10 for 32-bit int)
        SPACE   | O(1) constant extra space
*********************************************************
"""

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse integer with 32-bit overflow detection.

        Args:
            x: A signed 32-bit integer.

        Returns:
            Reversed integer, or 0 if overflow occurs.
        """
        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   #  2147483647

        result = 0
        # Work with positive copy, preserve sign separately
        sign = 1 if x >= 0 else -1
        x_abs = abs(x)

        while x_abs != 0:
            # Extract last digit
            digit = x_abs % 10
            x_abs //= 10

            # Check for overflow **before** adding the digit.
            # If result > INT_MAX//10, then result*10 will exceed INT_MAX.
            # If result == INT_MAX//10, then digit must not exceed last digit of INT_MAX (7 for positive).
            if result > INT_MAX // 10:
                return 0
            if result == INT_MAX // 10 and digit > INT_MAX % 10:
                return 0

            # Safe to multiply and add
            result = result * 10 + digit

        # Re‑apply sign
        result *= sign

        # Final bounds check (should be unnecessary due to earlier checks, but keep for safety)
        if result < INT_MIN or result > INT_MAX:
            return 0
        return result


if __name__ == "__main__":
    sol = Solution()

    # Provided test cases
    test_cases = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0),
        (1534236469, 0),      # overflow case
        (-2147483648, 0),     # overflow case (reversed 8463847412- outside range)
        (1463847412, 2147483641)  # edge case: max allowed reversed actually fits
    ]

    for x, expected in test_cases:
        result = sol.reverse(x)
        status = "✓" if result == expected else "✗"
        print(f"{status} reverse({x}) = {result}  (expected {expected})")