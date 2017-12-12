import unittest

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Ans = []
        self.assertEqual(Solution().mergeKLists(Input),Ans);
    def testEmptyList(self):
        Input = [[],[1,2],[]]
        Ans = [1,2]
        self.assertEqual(Solution().mergeKLists(Input),Ans);

class Solution():
    def mergeKLists(self, lists):
        Ans = []
        for item in lists:
            if item != []:
                Ans.extend(item)
        return Ans

if __name__ == '__main__':
    unittest.main()
