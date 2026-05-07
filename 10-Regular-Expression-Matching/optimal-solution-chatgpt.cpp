/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   May 7th, 2026
 *
 * LeetCode: #10 Regular Expression Matching
 *
 * Match entire string s against pattern p where:
 *
 *   '.' -> matches ANY single character
 *   '*' -> matches ZERO or MORE of previous character
 *
 * Examples:
 *   "aa"   vs "a"    -> false
 *   "aa"   vs "a*"   -> true
 *   "ab"   vs ".*"   -> true
 * 
 * 
 * Time and Space Complexity: Top-Down Dynamic Programming + Memoization
 * ------------------------------------------------------
 * Let:
 *   n = s.length()
 *   m = p.length()
 *
 * Time Complexity:
 *   O(n * m)
 *
 * Space Complexity:
 *   O(n * m)
 *
 * Why?
 *   Each state (i, j) is solved once and cached.
 *
 * ------------------------------------------------------
 * Compile & Run
 * ------------------------------------------------------
 * g++ -std=c++11 optimal-solution-chatgpt.cpp -o optimal-solution-chatgpt && ./optimal-solution-chatgpt
 *
 * ******************************************************
 */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:

    // memo[i][j]
    // -1 = unvisited
    //  0 = false
    //  1 = true
    vector<vector<int>> memo;

    bool isMatch(string s, string p) {

        // Create memo table
        memo.resize(s.size() + 1,
                    vector<int>(p.size() + 1, -1));

        return dfs(0, 0, s, p);
    }

private:

    /**
     * dfs(i, j)
     *
     * i = current index in string s
     * j = current index in pattern p
     */
    bool dfs(int i, int j, string& s, string& p) {

        // If already solved, return cached answer
        if (memo[i][j] != -1) {
            return memo[i][j];
        }

        // ------------------------------------------------
        // Base Case:
        // Pattern fully consumed
        // ------------------------------------------------
        if (j == p.size()) {

            // Match only succeeds if string ALSO finished
            return memo[i][j] = (i == s.size());
        }

        // ------------------------------------------------
        // Check if current chars match
        // ------------------------------------------------
        bool firstMatch = (
            i < s.size() &&
            (s[i] == p[j] || p[j] == '.')
        );

        // ------------------------------------------------
        // Handle '*' case
        // Example:
        //   a*
        //   .*
        // ------------------------------------------------
        if (j + 1 < p.size() && p[j + 1] == '*') {

            // Two choices:
            //
            // 1. Skip "x*"
            //      dfs(i, j+2)
            //
            // 2. Use current match and stay on pattern
            //      dfs(i+1, j)
            //
            // Why stay on j?
            // Because '*' can repeat MANY times.
            bool answer =
                dfs(i, j + 2, s, p) ||
                (firstMatch && dfs(i + 1, j, s, p));

            return memo[i][j] = answer;
        }

        // ------------------------------------------------
        // Normal character match
        // Move both pointers forward
        // ------------------------------------------------
        if (firstMatch) {
            return memo[i][j] =
                dfs(i + 1, j + 1, s, p);
        }

        // Otherwise: no match
        return memo[i][j] = false;
    }
};

int main() {

    Solution solution;

    // Test 1:
    // '*' repeating previous char
    cout << solution.isMatch("aa", "a*") << endl;
    // true


    // Test 2:
    // '.' matches any char
    cout << solution.isMatch("ab", ".*") << endl;
    // true


    // Test 3:
    // Complex mixed pattern
    cout << solution.isMatch("aab", "c*a*b") << endl;
    // true

    return 0;
}