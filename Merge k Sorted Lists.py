import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Ans = []
        self.assertEqual(Solution().mergeKLists(Input),Ans);

class Solution():
    def mergeKLists(self, lists):
        if lists == []:
            return []
        return None

if __name__ == '__main__':
    unittest.main()
