#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <regex>
#include <queue>
#include <map>

using namespace std;

int main()
{
	vector<vector<int> > envelopes = {
		{{15, 8}, {2, 20}, {2, 14}, {4, 17}, {8, 19}, {8, 9}, {5, 7}, {11, 19}, {8, 11}, {13, 11}, {2, 13}, {11, 19}, {8, 11}, {13, 11}, {2, 13}, {11, 19}, {16, 1}, {18, 13}, {14, 17}, {18, 19}} };


	vector<vector<int> > envelopes2 = {{5, 4},
									   {6, 4},
									   {6, 7},
									   {2, 3}};


	vector<vector<int> > envelopes3 = { {5, 7},
									   {8,9},
									   {13, 11},
									   {18, 13}, {19, 20} };


	vector<vector<int>> envelopes4 = {
		{{2, 100},{3, 200},{4, 300},{5, 500},{5, 400},{5, 250},{6, 370},{6, 360},{7, 380}}
	};
}
