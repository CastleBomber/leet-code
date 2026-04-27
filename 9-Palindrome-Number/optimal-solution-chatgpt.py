#!/usr/bin/env python3
"""
********************************************************
    Author: ChatGPT + CBOMBS
    Date:   April 25th, 2026

    LeetCode: #9 Palindrome Number

    Return True if integer x reads the same
    forward and backward.

    Example:
        121   -> True
        -121  -> False
        10    -> False

    ----------------------------------------------------
    Time / Space Complexity
    ----------------------------------------------------
    Let d = number of digits in x

    Time Complexity:
        O(d)
        - Reverse half the digits

    Space Complexity:
        O(1)
        - Only integer variables used

    ----------------------------------------------------
    Why This Is Optimal
    ----------------------------------------------------
    - No string conversion needed
    - Uses math only
    - Reverses only HALF the number
********************************************************
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers cannot be palindromes
        # Example: -121 != 121-
        if x < 0:
            return False

        # If number ends in 0, it cannot be palindrome
        # unless the number itself is 0
        # Example: 10 -> False
        if x != 0 and x % 10 == 0:
            return False

        reversed_half = 0

        # Build reversed second half of number
        # Stop when reversed_half catches up
        while x > reversed_half:

            digit = x % 10              # last digit
            reversed_half = reversed_half * 10 + digit

            x //= 10                   # remove last digit

        # For even digits:
        #   1221 -> x = 12, reversed_half = 12
        #
        # For odd digits:
        #   12321 -> x = 12, reversed_half = 123
        # Remove middle digit using //10
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    sol = Solution()

    # Test 1: even length palindrome
    print(sol.isPalindrome(1221))     # True

    # Test 2: negative number
    print(sol.isPalindrome(-121))     # False

    # Test 3: odd length palindrome
    print(sol.isPalindrome(12321))    # True