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
            Gets the maximum number from highest russian doll envelope set

            Using three different approaches to find max
            Envelopes are organized by:

            Sum of Sides
            Widths
            Heights

            Will compare the three countes and return the greater value
        */
        int maxEnvelopes(vector<vector<int>>& envelopes) {

            int countFromSumOfSides = 1;
            int countFromHeights = 1;
            int countFromWidths = 1;
            int greatestCount = 1;

            vector<vector<int>> envelopesBySumOfSides;
            vector<vector<int>> envelopesByHeights;
            vector<vector<int>> envelopesByWidths;

            envelopesBySumOfSides = sortEnvelopesBySumOfSides(envelopes);
            envelopesByHeights = sortEnvelopesByHeights(envelopes);
            envelopesByWidths = sortEnvelopesByWidths(envelopes);

            countFromSumOfSides = getRussianDollCount(envelopesBySumOfSides);
            countFromHeights = getRussianDollCount(envelopesByHeights);
            countFromWidths = getRussianDollCount(envelopesByWidths);

            greatestCount = getGreatestCount(countFromSumOfSides, countFromHeights, countFromWidths);

            return greatestCount;
        }

        /*
            sort each envelope in ascending order by sum of: height + width
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

        /*
            compares smallest height of sortedEnvelopes with the current envelope from envelopes,
            if the current envelope is smaller in height, it will be put in appropriately
            if the current envelope is larger in height, same deal
        */
        vector<vector<int>> sortEnvelopesByHeights(vector<vector<int>>& envelopes) {

            int i = 0;
            int j = 0;
            int smallHeight = 0;
            int currentHeight = 0;
            int smallWidth = 0;
            int currentWidth = 0;
            vector<vector<int>> sortedEnvelopes;

            sortedEnvelopes.push_back(envelopes[0]);

            for (i = 1; i < envelopes.size(); i++) {

                currentHeight = envelopes[i][0];
                currentWidth = envelopes[i][1];

                for (j = 0; j < sortedEnvelopes.size(); j++) {

                    smallHeight = sortedEnvelopes[j][0];
                    smallWidth = sortedEnvelopes[j][1];

                    if (currentHeight < smallHeight) {

                        sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
                        break;
                    }
                    else if (currentHeight == smallHeight) {

                        if (currentWidth < smallWidth) {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
                            break;
                        }
                    }
                }

                if ((currentHeight >= smallHeight) && (currentWidth >= smallWidth)) {

                    sortedEnvelopes.push_back(envelopes[i]);
                }
            }

            return sortedEnvelopes;

        }

        vector<vector<int>> sortEnvelopesByWidths(vector<vector<int>>& envelopes) {

            int i = 0;
            int j = 0;
            int smallHeight = 0;
            int currentHeight = 0;
            int smallWidth = 0;
            int currentWidth = 0;
            vector<vector<int>> sortedEnvelopes;

            sortedEnvelopes.push_back(envelopes[0]);

            for (i = 1; i < envelopes.size(); i++) {

                currentHeight = envelopes[i][0];
                currentWidth = envelopes[i][1];

                for (j = 0; j < sortedEnvelopes.size(); j++) {

                    smallHeight = sortedEnvelopes[j][0];
                    smallWidth = sortedEnvelopes[j][1];

                    if (currentWidth < smallWidth) {

                        sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
                        break;
                    }
                    else if (currentWidth == smallWidth) {

                        if (currentHeight < smallHeight) {

                            sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
                            break;
                        }
                    }
                }

                if ((currentWidth >= smallWidth) && (currentHeight >= smallHeight)) {

                    sortedEnvelopes.push_back(envelopes[i]);
                }
            }

            return sortedEnvelopes;
        }

        /*
            With envelopes now sorted,
            we will russian doll the envelopes to see how many can fit around eachother
            Each next envelope will need to be at least < H+1, W+1>

            ex1: in = [[2,3], [5,4], [6,4], [6,7]]     out = 3
                        ^A     ^B     ^B'    ^B''
        */
        int getRussianDollCount(vector<vector<int>>& envelopes) {

            int A = 0;
            int B = A + 1;
            int count = 1;
            vector<int> counts;

            counts.push_back(count); // handles 1 envelope case

            for (A = 0; A < envelopes.size(); A++) {

                if ((A+1) >= envelopes.size()) { break; } // exits if last envelope

                for (B = A + 1; B < envelopes.size(); B++) {

                    if(checkIfAFitsInsideB(envelopes[A], envelopes[B])) {

                        A = B;
                        count++;
                    }
                }

                counts.push_back(count); // reached the end, try with different envelopes
                count = 1;
            }

            count = getLargestCount(counts);

            return count;
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

        /*
            Takes in a vector as input and returns the largest value
        */
        int getLargestCount(vector<int> numbers) {

            int count = 0;

            for (int i = 0; i < numbers.size(); i++) {

                if (numbers[i] > count) {

                    count = numbers[i];
                }
            }

            return count;
        }
};


int main() {

    Solution solution;
    int count = 0; // russian doll'd envelopes

    vector<vector<int>> envelopes = { {{15,8},{2,20},{2,14},{4,17},{8,19},{8,9},{5,7},{11,19},{8,11},{13,11},
        {2,13},{11,19},{8,11},{13,11},{2,13},{11,19},{16,1},{18,13},{14,17},{18,19}} };

    count = solution.maxEnvelopes(envelopes);

    Node* root = new Node();

    cout << count << endl;
}
