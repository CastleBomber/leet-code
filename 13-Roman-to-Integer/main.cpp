/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   May 7th, 2026
 *
 * LeetCode: #13 Roman to Integer
 *
 * Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
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
 * For example, 2 is written as II in Roman numeral, just two ones added together. 
 * 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
 *
 * Roman numerals are usually written largest to smallest from left to right. 
 * However, the numeral for four is not IIII. Instead, the number four is written as IV. 
 * Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
 * There are six instances where subtraction is used:
 *
 * I can be placed before V (5) and X (10) to make 4 and 9. 
 * X can be placed before L (50) and C (100) to make 40 and 90. 
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 *
 * Given a roman numeral, convert it to an integer.
 *
 * 
 *
 * Example 1:
 *
 * Input: s = "III"
 * Output: 3
 * Explanation: III = 3.
 *
 * Example 2:
 *
 * Input: s = "LVIII"
 * Output: 58
 * Explanation: L = 50, V= 5, III = 3.
 *
 * Example 3:
 *
 * Input: s = "MCMXCIV"
 * Output: 1994
 * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 * 
 *
 * Constraints:
 *
 * 1 <= s.length <= 15
 * s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
 * It is guaranteed that s is a valid roman numeral in the range [1, 3999].
 * 
 * Compile and run:
 *   g++ -std=c++23 main.cpp -o main && ./main
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
 * Scan left to right, detect subtractive pairs (IV, IX, XL, XC, CD, CM) on the fly.
 * Unordered_map provides O(1) lookups for symbol values.
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

class Solution {
public:
    int romanToInt(string s) {
        // Special abilities with: 'C', 'X', 'I'
        unordered_map<char, int> roman_map = {
            {'M', 1000},
            {'D', 500},
            {'C', 100},
            {'L', 50},
            {'X', 10},
            {'V', 5},
            {'I', 1} 
        };

        int total = 0;

        for (int i = 0; i < s.length(); i++) {
            // Special case with 'C' (100) in front of 'M' (1000) or 'D' (500)
            if (s[i] == 'C') {
                if (s[i+1] == 'M' && i + 1 < s.length()) { 
                    total += 900;
                    i++;
                }
                else if (s[i+1] == 'D' && i + 1 < s.length()) {
                    total += 400;
                    i++;
                }
                else {
                    total += 100;
                }
            }

            // Special case with 'X' (10) in front of 'C' (100) or 'L' (50)
            else if (s[i] == 'X') {
                if (s[i+1] == 'C' && i + 1 < s.length()) {
                    total += 90;
                    i++;
                }
                else if (s[i+1] == 'L' && i + 1 < s.length()) { 
                    total += 40;
                    i++;
                }
                else {
                    total += 10;
                }
            }

            // Special case with 'I' (1) in front of 'X' (10) or 'V' (5)
            else if (s[i] == 'I') {
                if (s[i+1] == 'X' && i + 1 < s.length()) {
                    total += 9;
                    i++;
                }
                else if (s[i+1] == 'V' && i + 1 < s.length()) {
                    total += 4;
                    i++;
                }
                else {
                    total += 1;
                }
            }

            // Standartd 'M' (1000)
            else if (s[i] == 'M') {
                total += 1000;
            }

            // Standartd 'D' (500)
            else if (s[i] == 'D') {
                total += 500;
            }

            // Standartd 'L' (50)
            else if (s[i] == 'L') {
                total += 50;
            }

            // Standartd 'V' (5)
            else if (s[i] == 'V') {
                total += 5;
            }
        }

        return total;
    }
};

int main()
{
    Solution solution;

    string x = "III"; // 3
    string x2 = "CMXCIV"; // 994
    string x3 = "IX"; // 9
    string x4 = "IV"; // 4
    string x5 = "LVIII"; // 58

    cout << solution.romanToInt(x5) << endl;

    return 0;
}

