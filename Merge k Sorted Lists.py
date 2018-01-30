import unittest
import NodeSolution

class unitest(unittest.TestCase):
    def testNone(self):
        Input = []
        Ans = []
        self.assertEqual(Solution().mergeKLists(Input),Ans);
    def testEmptyList(self):
        Input = [[],[1,2],[]]
        Input = NodeSolution.NodeSolution().NodeList(Input)
        Ans = [1,2]
        self.assertEqual(Solution().mergeKLists(Input),Ans);
    def testSample(self):
        Input = [[1,3],[1,2],[5]]
        Input = NodeSolution.NodeSolution().NodeList(Input)
        Ans = [1,1,2,3,5]
        self.assertEqual(Solution().mergeKLists(Input),Ans);

class Solution():
    def mergeKLists(self, lists):
        Ans = []
        for items in lists:
            while items != None:
                Ans.append(items.val)
                items = items.next
        Ans.sort()
        return Ans

if __name__ == '__main__':
    unittest.main()
