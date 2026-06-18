/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   June 5th, 2026
 *
 * LeetCode: #14 Longest Common Prefix
 *
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 *
 *
 * Example 1:
 *
 * Input: strs = ["flower","flow","flight"]
 * Output: "fl"
 * Explanation: "fl" is the longest common prefix shared by all strings.
 *
 *
 * Example 2:
 *
 * Input: strs = ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 *
 * Constraints:
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] consists of only lowercase English letters if it is non-empty.
 *
 *
 * Compile and run:
 *   g++ -std=c++23 tmp.cpp -o tmp && ./tmp
 *
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
    string longestCommonPrefix(vector<string> &strs)
    {
        // Check if empty string
        if (strs.size() == 0)
        {
            return "";
        }

        // Check if only one string
        if (strs.size() == 1)
        {
            return strs[0];
        }

        // Sort by size
        sort(strs.begin(), strs.end(),
             [](const string &a, const string &b)
             {
                 return a.size() > b.size();
             });

        string output = "";

        // Load up first letter from strings
        int i = 0;
        char cur = strs[0][i];
        char next = strs[0][1];
        

        // Go through each of the strings
        for (int x = 0; x < strs.size(); x++)
        {
            // Make sure character exists
            if (x < strs[0].size())
            {
                return output;
            }

            if (cur == strs[1][0])
            {
                output += cur
            }
        }

        while (cur) {
            
            cur = strs[][];
            next = strs[][];
        }

            return output;
    }
};

int main()
{
    Solution solution;

    vector<string> strs1 = {"flower", "flow", "flight"};
    vector<string> strs2 = {"dog", "racecar", "car"};
    vector<string> strs3 = {"a"};

    cout << "Test 1: " << solution.longestCommonPrefix(strs1) << endl;
    cout << "Test 2: " << solution.longestCommonPrefix(strs2) << endl;
    cout << "Test 3: " << solution.longestCommonPrefix(strs3) << endl;

    return 0;
}