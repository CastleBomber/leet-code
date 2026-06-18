/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   June 5th, 2026
 *
 * LeetCode: #15 3Sum
 *
 * Given an integer array nums, return all the triplets 
 * [nums[i], nums[j], nums[k]] such that:
 *
 * i != j
 * i != k
 * j != k
 *
 * and
 *
 * nums[i] + nums[j] + nums[k] == 0
 *
 * Notice that the solution set must not contain duplicate triplets.
 *
 *
 *
 * Example 1:
 *
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation:
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
 *
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 *
 * Notice that the order of the output and the order of the triplets does not matter.
 *
 *
 * Example 2:
 *
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation:
 * The only possible triplet does not sum up to 0.
 *
 *
 * Example 3:
 *
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation:
 * The only possible triplet sums up to 0.
 *
 *
 * Constraints:
 *
 * 3 <= nums.length <= 3000
 * -10^5 <= nums[i] <= 10^5
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
    vector<vector<int>> threeSum(vector<int>& nums)
    {
        int i = nums[0];
        int j = nums[1];
        int k = nums[2];
        vector<vector<int>> outputs = {};

        for (int x = 0; x < nums.size(); x++) {
            if ((i + j + k) == 0) {
                outputs.push_back({i,j,k});
            }
        }

        return outputs;
    }
};

int main()
{
    Solution solution;

    vector<int> nums1 = {-1, 0, 1, 2, -1, -4};
    vector<int> nums2 = {0, 1, 1};
    vector<int> nums3 = {0, 0, 0};

    vector<vector<int>> result1 = solution.threeSum(nums1);
    vector<vector<int>> result2 = solution.threeSum(nums2);
    vector<vector<int>> result3 = solution.threeSum(nums3);

    cout << "Test 1 complete" << endl;
    cout << "Test 2 complete" << endl;
    cout << "Test 3 complete" << endl;

    return 0;
}