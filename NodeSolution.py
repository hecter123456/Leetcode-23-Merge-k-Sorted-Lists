import unittest

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class unitest(unittest.TestCase):
    def testNone(self):
        row = []
        l1 = NodeSolution().AddNode(row)
        self.assertEqual(l1,None);
    def testfirst(self):
        row = [2,4,3]
        l1 = NodeSolution().AddNode(row)
        self.assertEqual(l1.val,2);
        self.assertEqual(l1.next.val,4);
        self.assertEqual(l1.next.next.val,3);
"""
    def testNodeList(self):
        Input = [[1,3],[1,2],[5]]
        List = [NodeSolution().AddNode([1,3]),NodeSolution().AddNode([1,2]),NodeSolution().AddNode([5])]
        returnList = NodeSolution().NodeList(Input)
        self.assertEqual(returnList,List)
"""
class NodeSolution():
    def AddNode(self,row):
        addList = n = ListNode(0)
        for item in row:
            n.next = n = ListNode(item)
        return addList.next
    def NodeList(self,lists):
        List = []
        for item in lists:
            List.append(self.AddNode(item))
        return List

if __name__ == '__main__':
    unittest.main()
