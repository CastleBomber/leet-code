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

class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {

        int A = 0;
        int B = 0;
        int count = 1; // russian doll'd envelopes

        getSorted(envelopes); // sort by sum of H && W

        for(; A < envelopes.size(); A++) {

            if((A + 1) >= envelopes.size()) { break;} // check if last envelope

            for(B = A + 1; B < envelopes.size(); B++) {

                checkIfAFitsInB(envelopes[A], envelopes[B]);

                count++;
            }
        }

        return count;
    }

    /*
        sort by sume of H and W
    */
    vector<vector<int>> Envelopes getSorted(vector<vector<int>>& envelopes) {

        int sum = envelopeA[0] + envelopeB[1];

        return sum;
    }

    /**
     check if envelope A will fit in B
     needs to at least be B(A) ~ B(Wi + 1, Hi + 1) vs A(Wi, Hi)
    */
    int checkIfAFitsInB(vector<int> A, vector<int> B) {

    }
};
