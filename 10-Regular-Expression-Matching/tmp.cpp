/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   April 30th, 2026
 *
 * LeetCode: #10 Regular Expression Matching
 *
 * Given an input string s and a pattern p, implement regular expression
 * matching with support for '.' and '*' where:
 *
 *   - '.' Matches any single character.
 *   - '*' Matches zero or more of the preceding element.
 *
 * Return a boolean indicating whether the matching covers the entire input
 * string (not partial).
 *
 * Example 1:
 *   Input: s = "aa", p = "a"
 *   Output: false
 *   Explanation: "a" does not match the entire string "aa".
 *
 * Example 2:
 *   Input: s = "aa", p = "a*"
 *   Output: true
 *   Explanation: '*' means zero or more of the preceding element, 'a'.
 *                Therefore, by repeating 'a' once, it becomes "aa".
 *
 * Example 3:
 *   Input: s = "ab", p = ".*"
 *   Output: true
 *   Explanation: ".*" means "zero or more (*) of any character (.)".
 *
 * Constraints:
 *   - 1 <= s.length <= 20
 *   - 1 <= p.length <= 20
 *   - s contains only lowercase English letters.
 *   - p contains only lowercase English letters, '.', and '*'.
 *   - It is guaranteed for each appearance of the character '*', there will be
 *     a previous valid character to match.
 * 
 * Compile and run:
 *   g++ -std=c++11 tmp.cpp -o tmp && ./tmp
 *
 * Solution:
 * 
 * Notes
 *   string::npos (a special giant number) if NOT found
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

using namespace std;

class Solution {
public:
    /**
     * Check if the expression, P, equates to the entire string, S.
     * 
     * @param s - input string
     * @param p - pattern (regular expression)
     * @return bool - true if 
     */
    bool isMatch(string s, string p) {
        
        // Return true if strings are equal
        if (s == p) {
            return true;
        }

        // '.' Matches any single character
        if (s.find(".") != string::npos) {

        }
    
        // '*' Matches zero or more of the preceding element
        if (s.find("*") != string::npos) {

        }

        // Substring
        if (s.find(p) != string::npos) {

        }

        return true;
    }
};

int main() {
    Solution solution;
    string s = "aa";
    string p = "a";

    cout << solution.isMatch(s, p) << endl;
    return 0;
}