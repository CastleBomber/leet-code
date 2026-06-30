#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   June 28th, 2026

HackerRank
IBM Problem #2: Maximum Cost to Segregate a Binary String

You are given a binary string s containing only '0' and '1'.

The string is segregated when all '1' characters appear after
all '0' characters.

Operation:
    Choose a '1' and move it rightward until it reaches either:
        1. The end of the string
        2. The next '1' character

Cost:
    1 + number of positions the '1' moved

Goal:
    Compute the maximum total cost needed to segregate s.

Example:
    "10100" -> 8
    "01110" -> 6

Constraints:
    1 <= len(s) <= 10^5
    s[i] is either '0' or '1'

------------------------------------------------------
Time & Space Complexity: Single Pass + Zero Blocks
------------------------------------------------------
Let:           n = len(s)

Time Complexity:  O(n)       | Scan each character once
Space Complexity: O(1)       | Constant extra variables
------------------------------------------------------

********************************************************
"""


def getMaxCost(s: str) -> int:
    """
    Find the maximum cost to segregate a binary string.

    Args:
        s: Binary string containing only '0' and '1'.

    Returns:
        Maximum total cost to move all '1' characters right.
    """

    ones = 0
    cost = 0
    zero_block = False

    for ch in s:
        if ch == "1":
            ones += 1
            zero_block = False
        else:
            # Each earlier 1 must cross this 0.
            cost += ones

            # Each zero block lets every earlier 1 add one operation.
            if ones > 0 and not zero_block:
                cost += ones
                zero_block = True

    return cost


def main() -> None:
    # Test 1: problem example with mixed blocks
    # print(getMaxCost("10100"))    # 8

    # Test 2: problem example with one trailing zero
    # print(getMaxCost("01110"))    # 6

    # Test 3: already segregated
    print(getMaxCost("000111"))    # 0


main()
