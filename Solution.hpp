#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, int> leftHashMap, rightHashMap;
        unordered_set<string> unique_Palindromic_Strings;

        for(const char& ch: s) ++rightHashMap[ch];
        for(const char& ch: s) {
            --rightHashMap[ch];
            for(auto ptr = leftHashMap.begin(); ptr != leftHashMap.end(); ++ptr) {
                if(rightHashMap.find(ptr->first) != rightHashMap.end() && rightHashMap[ptr->first] > 0) {
                    string palindrome = string(1, ptr->first) + string(1, ch) + string(1, ptr->first);
                    unique_Palindromic_Strings.insert(palindrome);
                }
            }

            ++leftHashMap[ch];
        }

        return unique_Palindromic_Strings.size();
    }
};