/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   July 2nd, 2026
 *
 * LeetCode: #13 Roman to Integer
 *
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
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
 * Roman numerals are usually written largest to smallest from left to right.
 *
 * For example, 2 is written as II in Roman numeral, just two ones added together.
 * 12 is written as XII, which is simply X + II.
 * The number 27 is written as XXVII, which is XX + V + II.
 *
 * Roman numerals use subtractive notation in these cases:
 *
 * IV = 4
 * IX = 9
 * XL = 40
 * XC = 90
 * CD = 400
 * CM = 900
 *
 * Given a Roman numeral, convert it to an integer.
 *
 *
 * Key Idea:
 *
 * Scan the string from left to right
 *
 * If the current value is less than the next value,
 * subtract it from the total
 *
 * Otherwise,
 * add it to the total
 *
 * This handles subtractive pairs naturally
 *
 *
 * Example:
 * s = "MCMXCIV"
 *
 * M  = +1000
 * C  = -100   before M
 * M  = +1000
 * X  = -10    before C
 * C  = +100
 * I  = -1     before V
 * V  = +5
 *
 * Total = 1994
 *
 *
 * Constraints:
 *
 * 1 <= s length <= 15
 * s contains only I, V, X, L, C, D, M
 * s is guaranteed to be a valid Roman numeral from 1 to 3999
 *
 *
 * Compile and run:
 * g++ -std=c++23 optimal.cpp -o optimal && ./optimal
 *
 * Solution:
 * Accepted
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Single Pass with Lookup
 * ------------------------------------------------------
 * Let:           n = s length
 *
 * Time Complexity:  O(n)       | Visit each character once
 * Space Complexity: O(1)       | Fixed lookup table of 7 symbols
 * ------------------------------------------------------
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
    /**
     * Converts a Roman numeral string into an integer
     *
     * @param s - input Roman numeral string
     * @return total - integer value of the Roman numeral
     */
    int romanToInt(string s)
    {
        // Fixed lookup table for each Roman symbol
        static const unordered_map<char, int> romanMap = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}};

        int total = 0;

        // Compare each symbol with the symbol after it
        for (int i = 0; i < s.length(); i++)
        {
            int currentValue = romanMap.at(s[i]);

            // Subtract when this symbol belongs to a subtractive pair
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
    // string test1 = "III";
    // cout << "Input: " << test1 << endl;
    // cout << "Output: "
    //      << solution.romanToInt(test1)
    //      << endl;
    // cout << "Expected: 3\n"
    //      << endl;

    // Test Case 2: Additive Roman numeral
    // string test2 = "LVIII";
    // cout << "Input: " << test2 << endl;
    // cout << "Output: "
    //      << solution.romanToInt(test2)
    //      << endl;
    // cout << "Expected: 58\n"
    //      << endl;

    // Test Case 3: Multiple subtractive pairs
    string test3 = "MCMXCIV";
    cout << "Input: " << test3 << endl;
    cout << "Output: "
         << solution.romanToInt(test3)
         << endl;
    cout << "Expected: 1994\n"
         << endl;

    // Test Case 4: Multiple subtractive pairs
    string test4 = "MC";
    cout << "Input: " << test3 << endl;
    cout << "Output: "
         << solution.romanToInt(test4)
         << endl;
    cout << "Expected: *\n"
         << endl;


    return 0;
}
