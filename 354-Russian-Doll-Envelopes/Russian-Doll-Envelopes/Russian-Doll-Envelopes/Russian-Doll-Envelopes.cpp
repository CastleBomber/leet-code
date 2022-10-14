/*
    Author: CBOMBS
    Date: May 29th, 2022

    LeetCode: #354 - Russian Doll Envelopes

    You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

    One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

    Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

    Note: You cannot rotate an envelope.

    ex1: in = [[5,4],[6,4],[6,7],[2,3]]     out = 3
                ^A     ^B
*/

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <queue>

using namespace std;

struct Node {

    int key;
    vector<Node*> child;
};

Node *newNode (int key) {

    Node *tmp = new Node;
    tmp->key = key;

    return tmp;
}

class Solution {
    public:
        /*

        */
        int maxEnvelopes(vector<vector<int>>& envelopes) {

            int count = 1;
            vector<vector<int>> sortedEnvelopes;

            // take out duplicate envelopes, sort by height
            sortedEnvelopes.erase(unique(sortedEnvelopes.begin(), sortedEnvelopes.end()), sortedEnvelopes.end());
            sortedEnvelopes = sortEnvelopesByHeights(envelopes);

            // queue of general tree nodes with children being pointers to sub trees
            for (int A = 0; A < sortedEnvelopes.size(); A++) {

                if () {


                }
            }

            return count;
        }

        /*
            compares smallest height of sortedEnvelopes with the current envelope from envelopes,
            if the current envelope is smaller in height, it will be put in appropriately
            if the current envelope is larger in height, same deal
        */
        vector<vector<int>> sortEnvelopesByHeights(vector<vector<int>>& envelopes) {

            int e = 0; // envelopes position
            int sE = 0; // sortedEnvelopes position
            int sortedHeight = 0;
            int sortedWidth = 0;
            int unsortedHeight = 0;
            int unsortedWidth = 0;
            vector<vector<int>> sortedEnvelopes;

            sortedEnvelopes.push_back(envelopes[0]);

            // compare the unsorted envelopes with sortedEnvelopes
            for (e = 1; e < envelopes.size(); e++) {

                // take next from envelopes
                unsortedHeight = envelopes[e][0];
                unsortedWidth = envelopes[e][1];

                // compare with each in sortedEnvelopes, starts with smallest height
                for (sE = 0; sE < sortedEnvelopes.size(); sE++) {

                    sortedHeight = sortedEnvelopes[sE][0];
                    sortedWidth = sortedEnvelopes[sE][1];

                    if (unsortedHeight < sortedHeight) { // shorter

                        sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
                        break;
                    }
                    else if (unsortedHeight == sortedHeight) {

                        if (unsortedWidth <= sortedWidth) {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
                            break;
                        }
                        else {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + sE + 1, envelopes[e]);
                            break;
                        }
                    }
                    else if (unsortedHeight > sortedHeight) {
                        // no op
                    }

                    // have reached the end, tallest to add at the end
                    if ((sE+1) == sortedEnvelopes.size()) {

                        sortedEnvelopes.push_back(envelopes[e]);
                        break;
                    }
                }
            }

            return sortedEnvelopes;

        }

        /*
            compares smallest width of sortedEnvelopes with the current envelope from envelopes,
            if the current envelope is smaller in width, it will be put in appropriately
            if the current envelope is larger in width, same deal
        */
        vector<vector<int>> sortEnvelopesByWidths(vector<vector<int>>& envelopes) {

            int e = 0; // envelopes position
            int sE = 0; // sortedEnvelopes position
            int sortedHeight = 0;
            int sortedWidth = 0;
            int unsortedHeight = 0;
            int unsortedWidth = 0;
            vector<vector<int>> sortedEnvelopes;

            sortedEnvelopes.push_back(envelopes[0]);

            for (e = 1; e < envelopes.size(); e++) {

                unsortedHeight = envelopes[e][0];
                unsortedWidth = envelopes[e][1];

                for (sE = 0; sE < sortedEnvelopes.size(); sE++) {

                    sortedHeight = sortedEnvelopes[sE][0];
                    sortedWidth = sortedEnvelopes[sE][1];

                    if (unsortedWidth < sortedWidth) {

                        sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
                        break;
                    }
                    else if (unsortedWidth == sortedWidth) {

                        if (unsortedHeight < sortedHeight) {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
                            break;
                        }
                        else {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + sE + 1, envelopes[e]);
                            break;
                        }
                    }
                    else if (unsortedWidth > sortedWidth) {

                        // no op
                    }

                    // have reached the end, tallest to add at the end
                    if ((sE + 1) == sortedEnvelopes.size()) {

                        sortedEnvelopes.push_back(envelopes[e]);
                        break;
                    }
                }
            }

            return sortedEnvelopes;
        }

        /*
            sort each envelope in ascending order by sum of: height + width

            *algorithm could use more work
        */
        vector<vector<int>> sortEnvelopesBySumOfSides(vector<vector<int>>& envelopes) {

            int i = 1;
            int j = 0;
            int smallSum = 0;
            int currentSum = 0;
            vector<vector<int>> sortedEnvelopes;
            sortedEnvelopes.push_back(envelopes[0]);  // initial envelope's order position is '0'

            for (i = 1; i < envelopes.size(); i++) {

                currentSum = envelopes[i][0] + envelopes[i][1]; // sequential envelopes h + w

                for (j = 0; j < sortedEnvelopes.size(); j ++) { // order: initially <0>, then <0, 1, (^), 2, ...>

                    smallSum = sortedEnvelopes[j][0] + sortedEnvelopes[j][1];

                    if (currentSum < smallSum) {

                        sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
                        break;
                    }
                }

                if (currentSum >= smallSum) {

                    sortedEnvelopes.push_back(envelopes[i]);
                }

            }

            return sortedEnvelopes;
        }

        /**
             Checks if envelope A will fit inside B
             needs to at least be B(Wi + 1, Hi + 1) vs A(Wi, Hi)

             ex1:
             in = [[2,3], [5,4]     out = true
                    ^A     ^B


             ex2:
             in = [[5,4], [6,4]     out = false
                    ^A     ^B
        */
        int checkIfAFitsInsideB(vector<int> A, vector<int> B) {

            int heightA = A[0];
            int widthA = A[1];
            int heightB = B[0];
            int widthB = B[1];

            if((heightB > heightA) && (widthB > widthA)) {

                return 1;
            }

            return 0;
        }

        /*
            Takes in three integers && returns the greatest
        */
        int getGreatestCount(int a, int b, int c) {

            int greatest = a;

            if (b > greatest) {

                greatest = b;
            }

            if (c > greatest) {

                greatest = c;
            }

            return greatest;
        }
};

int main() {

    Solution solution;
    int count = 0; // russian doll'd envelopes

    vector<vector<int>> envelopes = {
        {{15,8},{2,20},{2,14},{4,17},{8,19},
        {8,9},{5,7},{11,19},{8,11},{13,11},
        {2,13},{11,19},{8,11},{13,11},{2,13},
        {11,19},{16,1},{18,13},{14,17},{18,19}} };

    count = solution.maxEnvelopes(envelopes);

    cout << count << endl;
}
