/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 3rd, 2026
 *
 * LeetCode: #13 Roman to Integer
 *
 * Roman numerals are represented by seven symbols:
 *
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 *
 * Roman numerals are generally written
 * largest → smallest from left to right.
 *
 * However, subtractive notation exists:
 *
 * IV = 4
 * IX = 9
 * XL = 40
 * XC = 90
 * CD = 400
 * CM = 900
 *
 * Key Idea:
 *
 * If the current Roman numeral is SMALLER than
 * the numeral to its right:
 *
 * subtract it.
 *
 * Otherwise:
 *
 * add it.
 *
 * Example:
 * s = "MCMXCIV"
 *
 * M  = +1000
 * C  = -100   (before M)
 * M  = +1000
 * X  = -10    (before C)
 * C  = +100
 * I  = -1     (before V)
 * V  = +5
 *
 * Total = 1994
 *
 *
 * Constraints:
 *
 * 1 <= s.length <= 15
 * s contains only:
 * ('I', 'V', 'X', 'L', 'C', 'D', 'M')
 *
 * Guaranteed valid Roman numeral
 * in range [1, 3999]
 *
 * Compile and run:
 * g++ -std=c++23 main.cpp -o main && ./main
 *
 * Solution:
 *     Accepted - 3999 / 3999 testcases passed
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Single Pass with Lookup
 * ------------------------------------------------------
 * Let:           n = s.length()  |  (1 <= n <= 15)
 *
 *
 * Time Complexity:  O(n)   | One pass through string, each char processed once
 * Space Complexity: O(1)   | Fixed map of 7 symbols + constant variables
 * ------------------------------------------------------
 *
 * Why Single Pass w/ Lookup?
 * Scan left to right and compare current value
 * against the next value.
 *
 * If current < next → subtract.
 * Otherwise → add.
 *
 * This automatically handles:
 * IV, IX, XL, XC, CD, and CM.
 *
 * ******************************************************
 */

#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        // Roman numeral lookup table
        static const unordered_map<char, int> romanMap = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}};

        int total = 0;

        // Traverse left → right
        for (int i = 0; i < s.length(); i++)
        {
            int currentValue = romanMap.at(s[i]);

            // Check if a next character exists
            // AND if current numeral should be subtractive
            if (i + 1 < s.length() &&
                currentValue < romanMap.at(s[i + 1]))
            {
                total -= currentValue;
            }
            else
            {
                total += currentValue;
            }
        }

        return total;
    }
};

int main()
{
    Solution solution;

    // Test Case 1: Basic repeated numerals
    string test1 = "III";
    cout << "Input: " << test1 << endl;
    cout << "Output: "
         << solution.romanToInt(test1)
         << endl;
    cout << "Expected: 3\n"
         << endl;

    // Test Case 2: Mixed standard + additive
    string test2 = "LVIII";
    cout << "Input: " << test2 << endl;
    cout << "Output: "
         << solution.romanToInt(test2)
         << endl;
    cout << "Expected: 58\n"
         << endl;

    // Test Case 3: Multiple subtractive cases
    string test3 = "MCMXCIV";
    cout << "Input: " << test3 << endl;
    cout << "Output: "
         << solution.romanToInt(test3)
         << endl;
    cout << "Expected: 1994\n"
         << endl;

    return 0;
}