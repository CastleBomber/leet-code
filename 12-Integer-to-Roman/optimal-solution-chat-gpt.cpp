/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 3rd, 2026
 *
 * LeetCode: #12 Integer to Roman
 *
 * Given an integer (1 <= num <= 3999),
 * convert it to a Roman numeral.
 *
 * Roman numerals use subtractive notation:
 *
 * 4   -> IV
 * 9   -> IX
 * 40  -> XL
 * 90  -> XC
 * 400 -> CD
 * 900 -> CM
 *
 * Key Idea:
 * Always subtract the LARGEST Roman value possible.
 *
 * Example:
 * num = 1994
 *
 * Start with largest values:
 *
 * 1994 - 1000 = 994   -> M
 * 994  - 900  = 94    -> CM
 * 94   - 90   = 4     -> XC
 * 4    - 4    = 0     -> IV
 *
 * Result = "MCMXCIV"
 *
 *
 * Constraints:
 * 1 <= num <= 3999
 *
 * Compile and run:
 * g++ -std=c++23 main.cpp -o main && ./main
 *
 * Solution:
 * Accepted - 3999 / 3999 testcases passed
 *
 * ------------------------------------------------------
 * Time and Space Complexity: Greedy + Lookup Table
 * ------------------------------------------------------
 * Let:
 *   n = num (1 <= n <= 3999)
 *
 * Time Complexity:
 *   O(1)
 *
 *   - Roman lookup table contains only 13 fixed values
 *   - Maximum Roman numeral length is bounded
 *   - Worst case is 3888:
 *
 *       MMMDCCCLXXXVIII
 *
 *     Which requires:
 *
 *       3(M) + 1(D) + 3(C)
 *     + 1(L) + 3(X)
 *     + 1(V) + 3(I)
 *     = 15 appends max
 *
 *   - Since input size is capped (3999),
 *     runtime is constant.
 *
 * Space Complexity:
 *   O(1)
 *
 *   - Fixed lookup table of 13 pairs
 *   - Result string max length is 15
 *   - Constant extra variables
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Greedy + Lookup Table
 * ------------------------------------------------------
 * Let:           n = num   | (1 <= n <= 3999)
 *
 * Time Complexity:  O(1)   | Max ~15 appends
 * Space Complexity: O(1)   | Fixed lookup table
 * ------------------------------------------------------
 *
 * Why Greedy + Lookup Table?
 *
 * Always subtract the LARGEST valid Roman value first.
 *
 * By precomputing subtractive forms:
 * (CM, CD, XC, XL, IX, IV)
 *
 * we eliminate special-case logic entirely.
 *
 * ******************************************************
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        // Ordered from LARGEST → SMALLEST
        // Includes subtractive forms to avoid special logic
        static const vector<pair<int, string>> roman = {
            {1000, "M"},
            {900, "CM"},
            {500, "D"},
            {400, "CD"},
            {100, "C"},
            {90, "XC"},
            {50, "L"},
            {40, "XL"},
            {10, "X"},
            {9, "IX"},
            {5, "V"},
            {4, "IV"},
            {1, "I"}};

        string result;
        int remaining = num;

        // Try largest Roman values first
        for (const auto &[value, symbol] : roman)
        {
            // Keep subtracting while possible
            while (remaining >= value)
            {
                result += symbol;
                remaining -= value;
            }

            // Early exit once fully converted
            if (remaining == 0)
            {
                break;
            }
        }

        return result;
    }
};

int main()
{
    Solution solution;

    // Test Case 1: Example case
    int test1 = 3749;
    cout << "Input: " << test1 << endl;
    cout << "Output: "
         << solution.intToRoman(test1)
         << endl;
    cout << "Expected: MMMDCCXLIX\n"
         << endl;

    // Test Case 2: Small edge case
    int test2 = 1;
    cout << "Input: " << test2 << endl;
    cout << "Output: "
         << solution.intToRoman(test2)
         << endl;
    cout << "Expected: I\n"
         << endl;

    // Test Case 3: Largest valid input
    int test3 = 3999;
    cout << "Input: " << test3 << endl;
    cout << "Output: "
         << solution.intToRoman(test3)
         << endl;
    cout << "Expected: MMMCMXCIX\n"
         << endl;

    return 0;
}