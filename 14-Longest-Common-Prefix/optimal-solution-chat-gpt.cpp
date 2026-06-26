/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 13th, 2026
 *
 * LeetCode: #14 Longest Common Prefix
 *
 * Write a function to find the longest common prefix string
 * amongst an array of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 *
 * Key Idea:
 *
 * The longest common prefix can NEVER be longer
 * than the shortest string in the vector.
 *
 * So:
 *
 * 1. Find the shortest string.
 * 2. Use each character in the shortest string as the reference.
 * 3. Compare that character against the same index
 *    in every other string.
 * 4. If there is a mismatch, return everything before that index.
 *
 *
 * Example:
 * strs = ["flower", "flow", "flight"]
 *
 * Shortest string = "flow"
 *
 * index 0:
 * f == f == f
 *
 * index 1:
 * l == l == l
 *
 * index 2:
 * o != i
 *
 * Stop.
 *
 * Return "fl"
 *
 *
 * Constraints:
 *
 * 1 <= strs.length <= 200
 * 0 <= strs[i].length <= 200
 * strs[i] consists of only lowercase English letters
 * if it is non-empty.
 *
 *
 * Compile and run:
 * g++ -std=c++23 optimal-solution-chat-gpt.cpp -o optimal-solution-chat-gpt && ./optimal-solution-chat-gpt
 *
 * Solution:
 * Accepted
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Shortest String + Vertical Scan
 * ------------------------------------------------------
 * Let:           n = strs.size()
 * Let:           m = shortest string length
 *
 * Time Complexity:  O(n * m)   | Compare each prefix char across all strings
 * Space Complexity: O(1)       | Constant extra variables
 * ------------------------------------------------------
 *
 * ******************************************************
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    /**
     * Finds the longest common prefix among all strings.
     *
     * @param strs - input vector of strings
     * @return shortest - longest common prefix
     */
    string longestCommonPrefix(vector<string>& strs)
    {
        // Start by assuming the first string is the shortest
        string shortest = strs[0];

        // Find the actual shortest string
        // The common prefix cannot be longer than this
        for (int i = 1; i < strs.size(); i++)
        {
            if (strs[i].size() < shortest.size())
            {
                shortest = strs[i];
            }
        }

        // Compare each character index of the shortest string
        for (int i = 0; i < shortest.size(); i++)
        {
            char currentChar = shortest[i];

            // Check this same character position in every string
            for (int j = 0; j < strs.size(); j++)
            {
                // If any string has a different character,
                // return everything before this index
                if (strs[j][i] != currentChar)
                {
                    return shortest.substr(0, i);
                }
            }
        }

        // If no mismatch was found,
        // the whole shortest string is the common prefix
        return shortest;
    }
};

int main()
{
    Solution solution;

    // Test Case 1: Normal shared prefix
    vector<string> test1 = {"flower", "flow", "flight"};
    cout << "Input: {\"flower\", \"flow\", \"flight\"}" << endl;
    cout << "Output: "
         << solution.longestCommonPrefix(test1)
         << endl;
    cout << "Expected: fl\n"
         << endl;

    // Test Case 2: No shared prefix
    vector<string> test2 = {"dog", "racecar", "car"};
    cout << "Input: {\"dog\", \"racecar\", \"car\"}" << endl;
    cout << "Output: "
         << solution.longestCommonPrefix(test2)
         << endl;
    cout << "Expected: \n"
         << endl;

    // Test Case 3: Single string edge case
    vector<string> test3 = {"a"};
    cout << "Input: {\"a\"}" << endl;
    cout << "Output: "
         << solution.longestCommonPrefix(test3)
         << endl;
    cout << "Expected: a\n"
         << endl;

    return 0;
}