/**
 * ******************************************************
 * Author: ChatGPT + CBOMBS
 * Date:   May 7th, 2026
 *
 * LeetCode: #11 Container With Most Water
 *
 * Given an array height, return the maximum amount
 * of water a container can store.
 *
 * Formula:
 *   area = width * min(height[left], height[right])
 *
 * ------------------------------------------------------
 * Time and Space Complexity: Two Pointers
 * ------------------------------------------------------
 * Let:
 *   n = height.size()
 *
 * Time Complexity:
 *   O(n)
 *   - Each pointer moves at most once across array
 *
 * Space Complexity:
 *   O(1)
 *   - Constant extra memory
 *
 * Why Two Pointers?
 *   Move the SHORTER wall inward.
 *   The shorter wall limits the water height.
 *
 * ******************************************************
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:

    int maxArea(vector<int>& height) {

        // Start with widest possible container
        int left = 0;
        int right = height.size() - 1;

        int maxWater = 0;

        while (left < right) {

            // Width between walls
            int width = right - left;

            // Water height limited by SHORTER wall
            int h = min(height[left], height[right]);

            // Current container area
            int area = width * h;

            // Store best answer seen so far
            maxWater = max(maxWater, area);

            // ------------------------------------------------
            // Move the SHORTER wall inward
            //
            // Why?
            // Taller wall does NOT help if shorter wall
            // is still limiting the water height.
            // ------------------------------------------------
            if (height[left] < height[right]) {
                left++;
            }
            else {
                right--;
            }
        }

        return maxWater;
    }
};

int main() {

    Solution solution;

    // Test 1: classic example
    vector<int> h1 = {1,8,6,2,5,4,8,3,7};
    cout << solution.maxArea(h1) << endl;
    // 49


    // Test 2: small/simple case
    vector<int> h2 = {1,1};
    cout << solution.maxArea(h2) << endl;
    // 1


    // Test 3: taller walls inside
    vector<int> h3 = {2,3,10,5,7,8,9};
    cout << solution.maxArea(h3) << endl;
    // 36

    return 0;
}