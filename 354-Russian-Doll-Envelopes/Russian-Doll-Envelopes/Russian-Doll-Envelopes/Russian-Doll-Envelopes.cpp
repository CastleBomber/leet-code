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


	Shortcuts:
	VS Code:
		c++ VS Code clang-formatter: shift+alt+f

	Visual Studio:
		code folding: select region, ctrl+m+m
		full screen: shift+alt+enter
*/

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <queue>

using namespace std;

struct Node
{
	int height;
	int width;
	vector<Node *> child;
};

Node *newNode(vector<int> envelope)
{
	Node *tmp = new Node;
	tmp->height = envelope[0];
	tmp->width = envelope[1];

	return tmp;
}

class Solution
{
public:
	/*
		Maximum number of envelopes that would fit inside eachother

				*
			   / \
			  *   *
			 / \
			*   *
	*/
	int maxEnvelopes(vector<vector<int> > &envelopes)
	{
		int count = 1; // Number of russian doll'd envelopes

		// Organize envelopes and remove duplicates
		vector<vector<int> > sortedEnvelopes;
		sortedEnvelopes = sortEnvelopesByHeights(envelopes);
		sortedEnvelopes.erase(unique(sortedEnvelopes.begin(), sortedEnvelopes.end()), sortedEnvelopes.end());

		// Used to create a descending general tree of nodes
		vector<Node *> initialQueue; // starting queue for each unique envelope
		vector<Node *> finalQueue;	// queue of nodes pointing to sub trees
		int position = 0;			// iterates through sortedEnvelopes

		// Load up the inital queue with unique envelopes
		for (position = 0; position < sortedEnvelopes.size(); position++)
		{
			Node *envelope = newNode(sortedEnvelopes[position]);
			initialQueue.push_back(envelope);
		}

		finalQueue = buildDescendingGeneralTree(initialQueue);

		// Traverse through general tree to find count
		/*for ()
		{
		}*/

		// Free up memory
		while (!initialQueue.empty())
		{
			initialQueue.erase(initialQueue.begin());
		}

		return count;
	}

	vector<Node *> buildDescendingGeneralTree(vector<Node *> startingQueue)
	{
		vector<Node *> initialQueue = startingQueue; // main queue loaded up from sortedEnvelopes
		vector<Node *> finalQueue;					//  final queue builds descending general tree
		vector<Node*> checkerQueue;					// tmp copy of final queue used to check if newly added has children 
		Node* frontInitialQueue;				// references first node of initial for push to final queue
		int initQPos = 0;						// iterates through inital queue
		int finalQPos = 0;							// iterates through final queue
		int childPosition = 0;						// node will have 0 to many children
		int sizeInitQ = initialQueue.size(); // determines number of envelope nodes to add

		// Build descending general tree
		for (initQPos = 0; initQPos < sizeInitQ - 1; initQPos++)
		{
			vector<Node *> checkerQueue = finalQueue; // will be a copy of finalQueue for children check
			frontInitialQueue = initialQueue.front(); // reference first node
			finalQueue.push_back(frontInitialQueue);			 	// add node to the back of final queue
			initialQueue.erase(initialQueue.begin());						// removes first node from initial quue
			childPosition = 0;

			for (finalQPos = 0; finalQPos < finalQueue.size() - 2; finalQPos++)
			{
				// Add child to the last envelope in finalQueue
				if (hasChildAbility(finalQueue.back(), checkerQueue.front()))
				{
					(finalQueue.back()->child).push_back(checkerQueue.front());
					childPosition++;
				}

				checkerQueue.erase(checkerQueue.begin());
			}
		}

		return finalQueue;
	}

	/*
		compares smallest height of sortedEnvelopes with the current envelope from envelopes,
		if the current envelope is smaller in height, it will be put in appropriately
		if the current envelope is larger in height, same deal
	*/
	vector<vector<int> > sortEnvelopesByHeights(vector<vector<int> > &envelopes)
	{
		int e = 0;	// envelopes position
		int sE = 0; // sortedEnvelopes position
		int sortedHeight = 0;
		int sortedWidth = 0;
		int unsortedHeight = 0;
		int unsortedWidth = 0;
		vector<vector<int> > sortedEnvelopes;

		sortedEnvelopes.push_back(envelopes[0]);

		// compare the unsorted envelopes with sortedEnvelopes
		for (e = 1; e < envelopes.size(); e++)
		{
			// take next from envelopes
			unsortedHeight = envelopes[e][0];
			unsortedWidth = envelopes[e][1];

			// compare with each in sortedEnvelopes, starts with smallest height
			for (sE = 0; sE < sortedEnvelopes.size(); sE++)
			{
				sortedHeight = sortedEnvelopes[sE][0];
				sortedWidth = sortedEnvelopes[sE][1];

				if (unsortedHeight < sortedHeight)
				{
					// shorter
					sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
					break;
				}
				else if (unsortedHeight == sortedHeight)
				{

					if (unsortedWidth <= sortedWidth)
					{
						sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
						break;
					}
					else
					{
						sortedEnvelopes.insert(sortedEnvelopes.begin() + sE + 1, envelopes[e]);
						break;
					}
				}
				else if (unsortedHeight > sortedHeight)
				{
					// no op
				}

				// have reached the end, tallest to add at the end
				if ((sE + 1) == sortedEnvelopes.size())
				{
					sortedEnvelopes.push_back(envelopes[e]);
					break;
				}
			}
		}

		return sortedEnvelopes;
	}

	vector<vector<int> > sortEnvelopesByWidths(vector<vector<int> > &envelopes)
	{
		int e = 0;	// envelopes position
		int sE = 0; // sortedEnvelopes position
		int sortedHeight = 0;
		int sortedWidth = 0;
		int unsortedHeight = 0;
		int unsortedWidth = 0;
		vector<vector<int> > sortedEnvelopes;

		sortedEnvelopes.push_back(envelopes[0]);

		for (e = 1; e < envelopes.size(); e++)
		{
			unsortedHeight = envelopes[e][0];
			unsortedWidth = envelopes[e][1];

			for (sE = 0; sE < sortedEnvelopes.size(); sE++)
			{
				sortedHeight = sortedEnvelopes[sE][0];
				sortedWidth = sortedEnvelopes[sE][1];

				if (unsortedWidth < sortedWidth)
				{
					sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
					break;
				}
				else if (unsortedWidth == sortedWidth)
				{
					if (unsortedHeight < sortedHeight)
					{
						sortedEnvelopes.insert(sortedEnvelopes.begin() + sE, envelopes[e]);
						break;
					}
					else
					{
						sortedEnvelopes.insert(sortedEnvelopes.begin() + sE + 1, envelopes[e]);
						break;
					}
				}
				else if (unsortedWidth > sortedWidth)
				{
					// no op
				}

				// have reached the end, tallest to add at the end
				if ((sE + 1) == sortedEnvelopes.size())
				{
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
	vector<vector<int> > sortEnvelopesBySumOfSides(vector<vector<int> > &envelopes)
	{
		int i = 1;
		int j = 0;
		int smallSum = 0;
		int currentSum = 0;
		vector<vector<int> > sortedEnvelopes;
		sortedEnvelopes.push_back(envelopes[0]); // initial envelope's order position is '0'

		for (i = 1; i < envelopes.size(); i++)
		{
			currentSum = envelopes[i][0] + envelopes[i][1]; // sequential envelopes h + w

			for (j = 0; j < sortedEnvelopes.size(); j++)
			{
				// order: initially <0>, then <0, 1, (^), 2, ...>
				smallSum = sortedEnvelopes[j][0] + sortedEnvelopes[j][1];

				if (currentSum < smallSum)
				{
					sortedEnvelopes.insert(sortedEnvelopes.begin() + j, envelopes[i]);
					break;
				}
			}

			if (currentSum >= smallSum)
			{
				sortedEnvelopes.push_back(envelopes[i]);
			}
		}

		return sortedEnvelopes;
	}

	/**
		 Checks if envelope A could have a child envelope B fit inside
		 needs to at least be A(Wi + 1, Hi + 1) vs B(Wi, Hi)

		 ex1:
		 in = [[5,4], [2,3]     out = true
				^A     ^B


		 ex2:
		 in = [[6,4], [5,4]     out = false
				^A     ^B
	*/
	int hasChildAbility(Node *A, Node *B)
	{

		int heightA = A->height;
		int widthA = A->width;
		int heightB = B->height;
		int widthB = B->width;

		if ((heightA > heightB) && (widthA > widthB))
		{
			return 1;
		}

		return 0;
	}

	/*
		Takes in three integers && returns the greatest
	*/
	int getGreatestCount(int a, int b, int c)
	{

		int greatest = a;

		if (b > greatest)
		{
			greatest = b;
		}

		if (c > greatest)
		{
			greatest = c;
		}

		return greatest;
	}
};

int main()
{
	Solution solution;
	int count = 0; // russian doll'd envelopes

	vector<vector<int> > envelopes = {
		{{15, 8}, {2, 20}, {2, 14}, {4, 17}, {8, 19}, 
		{8, 9}, {5, 7}, {11, 19}, {8, 11}, {13, 11}, 
		{2, 13}, {11, 19}, {8, 11}, {13, 11}, {2, 13}, {11, 19}, {16, 1}, {18, 13}, {14, 17}, {18, 19}}};

	count = solution.maxEnvelopes(envelopes);

	cout << count << endl;
}
