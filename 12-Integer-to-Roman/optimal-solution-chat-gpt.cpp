/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   July 1st, 2026
 *
 * LeetCode: #12 Integer to Roman
 *
 * Given an integer, convert it to a Roman numeral.
 *
 * Roman numerals are represented by seven different symbols:
 *
 * Symbol       Value
 * I            1
 * V            5
 * X            10
 * L            50
 * C            100
 * D            500
 * M            1000
 *
 * Roman numerals are usually written largest to smallest
 * from left to right.
 *
 * However, Roman numerals use subtractive notation for these cases:
 *
 * 4   -> IV
 * 9   -> IX
 * 40  -> XL
 * 90  -> XC
 * 400 -> CD
 * 900 -> CM
 *
 * Key Idea:
 *
 * Always subtract the LARGEST Roman value possible
 *
 * Store every important Roman value in descending order,
 * including the subtractive forms:
 *
 * CM, CD, XC, XL, IX, IV
 *
 * Then repeatedly append the largest symbol that fits
 * into the remaining number
 *
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
 *
 * 1 <= num <= 3999
 *
 *
 * Compile and run:
 * Use g++ with C++23 on this source file
 *
 * Solution:
 * Accepted
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
 * Always subtract the LARGEST valid Roman value first
 *
 * By precomputing subtractive forms:
 * (CM, CD, XC, XL, IX, IV)
 *
 * we eliminate special-case logic entirely
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
    /**
     * Converts an integer into its Roman numeral representation
     *
     * @param num - input integer from 1 to 3999
     * @return result - Roman numeral string
     */
    string intToRoman(int num)
    {
        // Ordered from largest to smallest
        // Subtractive forms are included so the greedy loop stays simple
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

        // Try each Roman value from largest to smallest
        for (const auto &[value, symbol] : roman)
        {
            // Append this symbol as many times as it fits
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
    // int test2 = 1;
    // cout << "Input: " << test2 << endl;
    // cout << "Output: "
    //      << solution.intToRoman(test2)
    //      << endl;
    // cout << "Expected: I\n"
    //      << endl;

    // Test Case 3: Largest valid input
    // int test3 = 3999;
    // cout << "Input: " << test3 << endl;
    // cout << "Output: "
    //      << solution.intToRoman(test3)
    //      << endl;
    // cout << "Expected: MMMCMXCIX\n"
    //      << endl;

    return 0;
}
