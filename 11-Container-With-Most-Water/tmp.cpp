/**
 * ******************************************************
 * Author: CBOMBS
 * Date:   April 30th, 2026
 *
 * LeetCode: #11 Container With Most Water
 *
 * You are given an integer array height of length n. There are n vertical
 * lines drawn such that the two endpoints of the ith line are (i, 0) and
 * (i, height[i]).
 *
 * Find two lines that together with the x-axis form a container, such that
 * the container contains the most water.
 *
 * Return the maximum amount of water a container can store.
 *
 * Notice that you may not slant the container.
 *
 * Example 1:
 *   Input: height = [1,8,6,2,5,4,8,3,7]
 *   Output: 49
 *   Explanation: The above vertical lines are represented by array
 *                [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
 *                the container can contain is 49.
 *
 * Example 2:
 *   Input: height = [1,1]
 *   Output: 1
 *
 * Constraints:
 *   - n == height.length
 *   - 2 <= n <= 10^5
 *   - 0 <= height[i] <= 10^4
 * 
 * Compile and run:
 *   g++ -std=c++11 tmp.cpp -o tmp && ./tmp
 *
 * Solution:
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
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maxWater = 0;
        return 0;
        
    }
};

int main() {
    Solution solution;
    vector<int> height = {1,8,6,2,5,4,8,3,7};

    cout << solution.maxArea(height) << endl;

    return 0;
}

