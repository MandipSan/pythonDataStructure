#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/04/2017

import unittest
from dataStructure.bSTree import *

class TestBSTree(unittest.TestCase):

   def setUp(self):
      self.bsTree = BSTree()

   def test_insertNode(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.assertEqual(self.bsTree.printInOrder(),"1,2,3")

   def test_removeNodeNoChildren(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.bsTree.removeNode(1)
      self.assertEqual(self.bsTree.printInOrder(),"2,3")

   def test_removeNodeTwoChildren(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(4)
      self.bsTree.insertNode(3)
      self.bsTree.removeNode(2)
      self.assertEqual(self.bsTree.printInOrder(),"1,3,4")

   def test_removeNodeLeftChild(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(4)
      self.bsTree.insertNode(3)
      self.bsTree.removeNode(4)
      self.assertEqual(self.bsTree.printInOrder(),"1,2,3")
      
   def test_removeNodeRightChild(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.bsTree.insertNode(0)
      self.bsTree.removeNode(0)
      self.assertEqual(self.bsTree.printInOrder(),"1,2,3")

   def test_findSmallestNodeData(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(4)
      self.bsTree.insertNode(3)
      self.assertEqual(self.bsTree.findSmallestNodeData(self.bsTree.root),1)

   def test_printPreOrder(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.assertEqual(self.bsTree.printPreOrder(),"2,1,3")
      
   def test_printPostOrder(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.assertEqual(self.bsTree.printPostOrder(),"1,3,2")

   def test_printAllLevel(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.bsTree.insertNode(6)
      self.bsTree.insertNode(5)
      self.assertEqual(self.bsTree.printAllLevel(),"2,1,3,6,5")
      
   def test_printOneLevel(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.bsTree.insertNode(6)
      self.bsTree.insertNode(5)
      self.assertEqual(self.bsTree.printOneLevel(2),"1,3")

   def test_getHeight(self):
      self.bsTree.insertNode(2)
      self.bsTree.insertNode(1)
      self.bsTree.insertNode(3)
      self.bsTree.insertNode(6)
      self.bsTree.insertNode(5)
      self.assertEqual(self.bsTree.getHeight(self.bsTree.root),4)

   def test_recInsertNode(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintInOrder(self.bsTree.root),"1,2,3")

   def test_recRemoveNodeNoChildren(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recRemoveNode(1,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintInOrder(self.bsTree.root),"2,3")

   def test_recRemoveNodeTwoChildren(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(4,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recRemoveNode(2,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintInOrder(self.bsTree.root),"1,3,4")

   def test_recRemoveNodeLeftChild(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(4,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recRemoveNode(4,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintInOrder(self.bsTree.root),"1,2,3")
      
   def test_recRemoveNodeRightChild(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(0,self.bsTree.root)
      self.bsTree.root = self.bsTree.recRemoveNode(0,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintInOrder(self.bsTree.root),"1,2,3")

   def test_recFindSmallestNodeData(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(4,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.assertEqual(self.bsTree.recFindSmallestNodeData(self.bsTree.root),1)

   def test_recPrintPreOrder(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintPreOrder(self.bsTree.root),"2,1,3")
      
   def test_recPrintPostOrder(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintPostOrder(self.bsTree.root),"1,3,2")

   def test_recPrintAllLevel(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(6,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(5,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintAllLevel(),"2,1,3,6,5")
      
   def test_recPrintOneLevel(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(6,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(5,self.bsTree.root)
      self.assertEqual(self.bsTree.recPrintOneLevel(self.bsTree.root,2),"1,3")

   def test_recGetHeight(self):
      self.bsTree.root = self.bsTree.recInsertNode(2,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(1,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(3,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(6,self.bsTree.root)
      self.bsTree.root = self.bsTree.recInsertNode(5,self.bsTree.root)
      self.assertEqual(self.bsTree.recGetHeight(self.bsTree.root),4)

if __name__ == '__main__':
   print "BSTree Testing"
   unittest.main()
