from timeout_decorator import timeout
from Solution import Solution
import unittest

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testcases = {1: ('aabca', 3), 2: ('adc', 0), 3: ('bbcbaba', 4)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_case_1(self):
        s, output = self.__testcases[1]
        result = self.__obj.countPalindromicSubsequence(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_2(self):
        s, output = self.__testcases[2]
        result = self.__obj.countPalindromicSubsequence(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_case_3(self):
        s, output = self.__testcases[3]
        result = self.__obj.countPalindromicSubsequence(s = s)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()