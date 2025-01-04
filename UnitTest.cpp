#include <iostream>
#include "Solution.hpp"

struct testcase {
    string s;
    int output;
};

class UnitTest {
private:
    vector<testcase> testcases;
    Solution obj;
public:
    UnitTest() {
        testcases = {{"aabca", 3}, {"adc", 0}, {"bbcbaba", 4}};
    }

    void test() {
        for(int i = 0; i < testcases.size(); ++i) {
            int result = obj.countPalindromicSubsequence(testcases[i].s);
            cout << "TestCase " << i+1 << ": " << ((result == testcases[i].output) ? "passed":"failed") << endl;
        }
    }
};

int main() {
    UnitTest test;
    test.test();
}