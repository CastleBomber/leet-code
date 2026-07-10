/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   July 9th, 2026
 *
 * LeetCode: #14 Longest Common Prefix
 *
 * Write a function to find the longest common prefix string amongst an array of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 *
 * Key Idea:
 *
 * The longest common prefix can never be longer
 * than the shortest string in the vector
 *
 * So:
 *
 * 1 - Find the shortest string
 * 2 - Use each character in the shortest string as the reference
 * 3 - Compare that character against the same index
 *    in every other string
 * 4 - If there is a mismatch, return everything before that index
 *
 *
 * Example:
 * strs = ["flower", "flow", "flight"]
 *
 * Use the shortest string as the reference:
 * reference = "flow"
 *
 * index 0:
 * flower[0] == flow[0] == flight[0]
 * f == f == f
 *
 * index 1:
 * flower[1] == flow[1] == flight[1]
 * l == l == l
 *
 * index 2:
 * flower[2] == flow[2]
 * flower[2] != flight[2]
 * o != i
 *
 * Mismatch found at index 2
 *
 * Return "fl"
 *
 *
 * Constraints:
 *
 * 1 <= strs length <= 200
 * 0 <= each string length <= 200
 * Each string consists of lowercase English letters when non-empty
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
 * Time & Space Complexity: Shortest String + Vertical Scan
 * ------------------------------------------------------
 * Let:           n = strs size
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

using namespace std;

class Solution
{
public:
    /**
     * Finds the longest common prefix among all strings
     *
     * @param strs - input vector of strings
     * @return shortest - longest common prefix
     */
    string longestCommonPrefix(vector<string> &strs)
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
                // Return the prefix before the first mismatch
                if (strs[j][i] != currentChar)
                {
                    return shortest.substr(0, i);
                }
            }
        }

        // If no mismatch was found, the whole shortest string is the answer
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
    // vector<string> test2 = {"dog", "racecar", "car"};
    // cout << "Input: {\"dog\", \"racecar\", \"car\"}" << endl;
    // cout << "Output: "
    //      << solution.longestCommonPrefix(test2)
    //      << endl;
    // cout << "Expected: \n"
    //      << endl;

    // Test Case 3: Single string edge case
    // vector<string> test3 = {"a"};
    // cout << "Input: {\"a\"}" << endl;
    // cout << "Output: "
    //      << solution.longestCommonPrefix(test3)
    //      << endl;
    // cout << "Expected: a\n"
    //      << endl;

    // Test Case 4: Single string edge case
    // vector<string> test4 = {"xabc", "yabc", "zabc"};
    // cout << "Input: {\"xabc\", \"yabc\", \"zabc\"}" << endl;
    // cout << "Output: "
    //      << solution.longestCommonPrefix(test4)
    //      << endl;
    // cout << "Expected: *\n"
    //      << endl;

    return 0;
}
