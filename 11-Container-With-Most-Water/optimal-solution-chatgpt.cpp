/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   June 26th, 2026
 *
 * LeetCode: #11 Container With Most Water
 *
 * You are given an integer array height of length n.
 *
 * There are n vertical lines drawn such that the two endpoints
 * of the ith line are (i, 0) and (i, height[i]).
 *
 * Find two lines that together with the x-axis form a container,
 * such that the container contains the most water.
 *
 * Return the maximum amount of water a container can store.
 *
 * Notice:
 * You may not slant the container.
 *
 *
 * Key Idea:
 *
 * Use two pointers at the widest possible container:
 *
 * left  = 0
 * right = height.size() - 1
 *
 * At each step:
 *
 * 1. Calculate the current area.
 * 2. Keep track of the largest area seen so far.
 * 3. Move the pointer at the SHORTER wall inward.
 *
 * Why move the shorter wall?
 *
 * The shorter wall limits the water height.
 * Moving the taller wall inward only makes the width smaller
 * while the same shorter wall is still limiting the container.
 *
 *
 * Example:
 * height = [1,8,6,2,5,4,8,3,7]
 *
 * Best container:
 * left  = index 1, height = 8
 * right = index 8, height = 7
 *
 * width  = 8 - 1 = 7
 * height = min(8, 7) = 7
 *
 * area = 7 * 7 = 49
 *
 * Return 49
 *
 *
 * Constraints:
 *
 * n == height.length
 * 2 <= n <= 10^5
 * 0 <= height[i] <= 10^4
 *
 *
 * Compile and run:
 * g++ -std=c++23 optimal-solution-chatgpt.cpp -o optimal-solution-chatgpt && ./optimal-solution-chatgpt
 *
 * Solution:
 * Accepted
 *
 *
 * ------------------------------------------------------
 * Time & Space Complexity: Two Pointers
 * ------------------------------------------------------
 * Let:           n = height.size()
 *
 * Time Complexity:  O(n)       | Each pointer moves inward at most n times
 * Space Complexity: O(1)       | Constant extra variables
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
     * Finds the maximum water area formed by two vertical lines.
     *
     * @param height - input vector of wall heights
     * @return maxWater - maximum amount of water the container can store
     */
    int maxArea(vector<int>& height)
    {
        // Start with the widest possible container
        int left = 0;
        int right = height.size() - 1;

        int maxWater = 0;

        while (left < right)
        {
            // Width is the distance between the two selected lines
            int width = right - left;

            // The shorter wall determines how high the water can be
            int currentHeight = min(height[left], height[right]);

            // Area of the current container
            int currentWater = width * currentHeight;

            // Keep the best answer seen so far
            maxWater = max(maxWater, currentWater);

            // Move the limiting wall inward to search for a taller boundary
            if (height[left] < height[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }

        return maxWater;
    }
};

int main()
{
    Solution solution;

    // Test Case 1: Classic example from the problem
    vector<int> test1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << "Input: {1, 8, 6, 2, 5, 4, 8, 3, 7}" << endl;
    cout << "Output: "
         << solution.maxArea(test1)
         << endl;
    cout << "Expected: 49\n"
         << endl;

    // Test Case 2: Smallest valid input
    vector<int> test2 = {1, 1};
    cout << "Input: {1, 1}" << endl;
    cout << "Output: "
         << solution.maxArea(test2)
         << endl;
    cout << "Expected: 1\n"
         << endl;

    // Test Case 3: Best answer uses inner walls, not the outermost pair
    vector<int> test3 = {2, 3, 10, 5, 7, 8, 9};
    cout << "Input: {2, 3, 10, 5, 7, 8, 9}" << endl;
    cout << "Output: "
         << solution.maxArea(test3)
         << endl;
    cout << "Expected: 36\n"
         << endl;

    return 0;
}
