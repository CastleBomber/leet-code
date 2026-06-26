/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 14th, 2026
 *
 * LeetCode: #15 3Sum
 *
 * Given an integer array nums, return all unique triplets
 * [nums[i], nums[j], nums[k]] such that:
 *
 * nums[i] + nums[j] + nums[k] == 0
 *
 * The solution set must not contain duplicate triplets.
 *
 *
 * Key Idea:
 *
 * Sort the array.
 *
 * Then fix one number nums[i], and use two pointers:
 *
 * left  = i + 1
 * right = nums.size() - 1
 *
 * If sum < 0, move left forward.
 * If sum > 0, move right backward.
 * If sum == 0, save the triplet.
 *
 *
 * Example:
 * nums = [-1, 0, 1, 2, -1, -4]
 *
 * Sorted:
 * nums = [-4, -1, -1, 0, 1, 2]
 *
 * Output:
 * [[-1,-1,2],[-1,0,1]]
 *
 *
 * Constraints:
 *
 * 3 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
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
 * Time & Space Complexity: Sort + Two Pointers
 * ------------------------------------------------------
 * Let:           n = nums.size()
 *
 * Time Complexity:  O(n^2)     | Sort + two-pointer scan
 * Space Complexity: O(log n)   | Sort stack, excluding answer
 * ------------------------------------------------------
 *
 * ******************************************************
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    /**
     * Finds all unique triplets that sum to zero.
     *
     * @param nums - input vector of integers
     * @return result - vector of unique triplets
     */
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        vector<vector<int>> result;

        // Sort first so duplicate values are next to each other
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {
            // Skip duplicate fixed numbers
            if (i > 0 && nums[i] == nums[i - 1])
            {
                continue;
            }

            // If nums[i] is positive, all numbers after it are positive too
            if (nums[i] > 0)
            {
                break;
            }

            int left = i + 1;
            int right = nums.size() - 1;

            // Find two numbers that pair with nums[i]
            while (left < right)
            {
                int sum = nums[i] + nums[left] + nums[right];

                if (sum == 0)
                {
                    result.push_back({nums[i], nums[left], nums[right]});

                    left++;
                    right--;

                    // Skip duplicate left values
                    while (left < right && nums[left] == nums[left - 1])
                    {
                        left++;
                    }

                    // Skip duplicate right values
                    while (left < right && nums[right] == nums[right + 1])
                    {
                        right--;
                    }
                }
                else if (sum < 0)
                {
                    // Need a bigger sum
                    left++;
                }
                else
                {
                    // Need a smaller sum
                    right--;
                }
            }
        }

        return result;
    }
};

/**
 * Prints a 2D vector in LeetCode-style format.
 *
 * @param result - vector of triplets
 * @return void
 */
void print2DVector(const vector<vector<int>>& result)
{
    cout << "[";

    for (int i = 0; i < result.size(); i++)
    {
        cout << "[";

        for (int j = 0; j < result[i].size(); j++)
        {
            cout << result[i][j];

            if (j < result[i].size() - 1)
            {
                cout << ",";
            }
        }

        cout << "]";

        if (i < result.size() - 1)
        {
            cout << ",";
        }
    }

    cout << "]";
}

int main()
{
    Solution solution;

    // Test Case 1: Normal case with two valid triplets
    vector<int> test1 = {-1, 0, 1, 2, -1, -4};
    cout << "Input: {-1, 0, 1, 2, -1, -4}" << endl;
    cout << "Output: ";
    print2DVector(solution.threeSum(test1));
    cout << endl;
    cout << "Expected: [[-1,-1,2],[-1,0,1]]\n"
         << endl;

    // Test Case 2: No valid triplet
    vector<int> test2 = {0, 1, 1};
    cout << "Input: {0, 1, 1}" << endl;
    cout << "Output: ";
    print2DVector(solution.threeSum(test2));
    cout << endl;
    cout << "Expected: []\n"
         << endl;

    // Test Case 3: All zeroes
    vector<int> test3 = {0, 0, 0};
    cout << "Input: {0, 0, 0}" << endl;
    cout << "Output: ";
    print2DVector(solution.threeSum(test3));
    cout << endl;
    cout << "Expected: [[0,0,0]]\n"
         << endl;

    return 0;
}