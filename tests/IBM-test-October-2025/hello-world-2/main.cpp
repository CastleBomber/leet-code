#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>

using namespace std;

/*
 *  sent - I choose a lazy person to do a hard job
 *  received - choose a person hard
 *  
 *  returns ["I", "a", "lazy", "to", "do", "job"]
 */
vector<string> lostFragments(string sent, string received) { 
    vector<string> words; stringstream ss(sent); string word; 
    // Get words, split by spaces 
    while (ss >> word) { words.push_back(word); } 
    // Remove received words from sent words 
    stringstream rs(received); 
    string rword; while( rs >> rword) { auto it = find(words.begin(), words.end(), rword); if (it != words.end()) { words.erase(it); } } for (string word : words) { cout << word << endl; } 
    return words; }






int main() {
    vector<string> result;
    string sent = "I choose a lazy person to do a hard job";
    string received = "choose a person hard";
    result = lostFragments(sent, received);

    return 0;
}