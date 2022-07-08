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

        int count = 1; // russian doll'd envelopes

        sortEnvelopes(envelopes);
        count = getRussianDollCount(envelopes);

        return count;
    }

    /*
        sort by sum: H + W
    */
    void sortEnvelopes(vector<vector<int>>& envelopes) {

        vector<int> rowSums;

        for(int i = 0; i < envelopes.size(); i++) {

            rowSums.push_back(envelopes[i] + envelopes[i+1]);
        }

        int smallest = 0;

        for(int j = 0; j < rowSums.size(); rowSums++) {

            if(smallest < rowSums[j]) {

                
            }
        }

        return sum;
    }

    int getRussianDollCount(vector<vector<int>>& envelopes) {

      int A = 0;
      int B = 0;
      int count = 0;

      for(; A < envelopes.size(); A++) {

          if((A + 1) >= envelopes.size()) { break;} // check if last envelope

          for(B = A + 1; B < envelopes.size(); B++) {

              checkIfAFitsInB(envelopes[A], envelopes[B]);

              count++;
          }
      }

      return count;

    }

    /**
     check if envelope A will fit in B
     needs to at least be B(A) ~ B(Wi + 1, Hi + 1) vs A(Wi, Hi)
    */
    int checkIfAFitsInB(vector<int> A, vector<int> B) {


    }
};
