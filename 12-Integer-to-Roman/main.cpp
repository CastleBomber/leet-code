/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   May 7th, 2026
 *
 * LeetCode: #12 Integer to Roman
 *
 * Seven different symbols represent Roman numerals with the following values:
 *
 * Symbol	Value
 * I	     1
 * V	     5
 * X	     10
 * L         50
 * C	     100
 * D	     500
 * M	     1000
 *
 * Roman numerals are formed by appending the conversions of 
 * decimal place values from highest to lowest. 
 * 
 * Converting a decimal place value into a Roman numeral has the following rules:
 *
 * If the value does not start with 4 or 9, 
 * select the symbol of the maximal value that can be subtracted from the input, 
 * append that symbol to the result, 
 * subtract its value, and convert the remainder to a Roman numeral.
 * 
 * If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, 
 * for example, 
 * 4 is 1 (I) less than 5 (V): IV and 
 * 9 is 1 (I) less than 10 (X): IX. 
 * 
 * Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
 * 
 * Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. 
 * You cannot append 5 (V), 50 (L), or 500 (D) multiple times. 
 * 
 * If you need to append a symbol 4 times use the subtractive form.
 * 
 * Given an integer, convert it to a Roman numeral.
 *
 *
 *
 * Example 1:
 * Input: num = 3749
 * Output: "MMMDCCXLIX"
 * Explanation:
 *      3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 *       700 = DCC as 500 (D) + 100 (C) + 100 (C)
 *        40 = XL as 10 (X) less of 50 (L)
 *         9 = IX as 1 (I) less of 10 (X)
 *
 * Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
 *
 *
 * Example 2:
 * Input: num = 58
 * Output: "LVIII"
 * Explanation:
 * 50 = L
 *  8 = VIII
 *
 *
 * Example 3:
 * Input: num = 1994
 * Output: "MCMXCIV"
 * Explanation:
 * 1000 = M
 *  900 = CM
 *   90 = XC
 *    4 = IV
 *
 *
 * Constraints:
 * 1 <= num <= 3999
 *
 * Compile and run:
 *   g++ -std=c++23 main.cpp -o main && ./main
 *
 * Solution:
 *   Accepted - 3999 / 3999 testcases passed
 * 
 * ------------------------------------------------------
 * Time and Space Complexity: Greedy with Lookup Table
 * ------------------------------------------------------
 * Let:
 *   n = num (1 <= n <= 3999)
 *
 * Time Complexity:
 *   O(1)
 *   - While loop runs at most 15 iterations per test case
 *   - Because the largest number (3999 = MMMCMXCIX) requires:
 *     3 (M) + 1 (CM) + 1 (D) + 1 (CD) + 1 (C) + 1 (XC) + 1 (L) + 1 (XL) + 1 (X) + 1 (IX) + 1 (V) + 1 (IV) + 1 (I)
 *     = 15 subtractions TOTAL
 *   - This is constant, independent of input size within constraints
 *
 * Space Complexity:
 *   O(1)
 *   - 13 fixed pairs in lookup table (constant memory)
 *   - result string max length 15 characters
 *   - Only a few integer variables
 *
 * Why Greedy with Lookup Table?
 *   Always subtract the LARGEST possible Roman value first.
 *   The subtractive forms (CM, CD, XC, XL, IX, IV) are precomputed,
 *   eliminating special case logic for 4s and 9s.
 *
 * 
 * ------------------------------------------------------
 * Time & Space Complexity: Greedy with Lookup Table
 * ------------------------------------------------------
 * Let:           n = num   |  (1 <= n <= 3999)
 * 
 * 
 * Time Complexity:  O(1)   | Max 15 iterations (3999 → MMMCMXCIX)
 * Space Complexity: O(1)   | Fixed 13 pairs + constant variables
 * ------------------------------------------------------
 * 
 * Why Greedy w/ Lookup Table? 
 * Subtract LARGEST possible value first.
 * Precomputed subtractive forms (CM, XC, IX, etc.) eliminate 4/9 logic.
 * 
 * ******************************************************
 */

#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    string intToRoman(int num)
    {
        vector<pair<string, int>> roman = {
            {"M", 1000}, {"CM", 900}, {"D", 500}, {"CD", 400},
            {"C", 100}, {"XC", 90}, {"L", 50}, {"XL", 40},
            {"X", 10}, {"IX", 9}, {"V", 5}, {"IV", 4}, {"I", 1}
        };

        int tmp = num;
        string result = "";

        for (const auto& [symbol, value] : roman) {
            while (tmp >= value) {
                result += symbol;
                tmp = tmp - value;
            }
        }

        return result;
    }
};

int main()
{
    Solution solution;
    int x = 3749;
    cout << solution.intToRoman(x) << endl; // MMMDCCXLIX

    return 0;
}
