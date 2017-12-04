#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/04/2017

import unittest
from dataStructure.aVLTree import *

class TestAVLTree(unittest.TestCase):

   def setUp(self):
      self.avlTree = AVLTree()

   def test_insertNodeLeftLeftCase(self):
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(7)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(5)
      self.avlTree.insertNode(1)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,6,1,5,7")

   def test_insertNodeLeftRightCase(self):
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(7)
      self.avlTree.insertNode(1)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(3)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,6,1,3,7")

   def test_insertNodeRightRightCase(self):
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(1)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(3)
      self.avlTree.insertNode(5)
      self.avlTree.insertNode(6)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,5,1,3,6")

   def test_insertNodeRightLeftCase(self):
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(1)
      self.avlTree.insertNode(5)
      self.avlTree.insertNode(3)
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(4)
      self.assertEqual(self.avlTree.printAllLevel(),"3,2,5,1,4,6")

   def test_removeNodeLeftLeftCase(self):
      self.avlTree.insertNode(8)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(12)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(10)
      self.avlTree.insertNode(13)
      self.avlTree.insertNode(1)
      self.avlTree.insertNode(3)
      self.avlTree.removeNode(10)
      self.avlTree.removeNode(13)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,8,1,3,6,12")

   def test_removeNodeLeftRightCase(self):
      self.avlTree.insertNode(8)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(12)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(10)
      self.avlTree.insertNode(13)
      self.avlTree.insertNode(5)
      self.avlTree.insertNode(7)
      self.avlTree.removeNode(10)
      self.avlTree.removeNode(13)
      self.assertEqual(self.avlTree.printAllLevel(),"6,4,8,2,5,7,12")

   def test_removeNodeRightRightCase(self):
      self.avlTree.insertNode(8)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(12)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(10)
      self.avlTree.insertNode(14)
      self.avlTree.insertNode(13)
      self.avlTree.insertNode(15)
      self.avlTree.removeNode(2)
      self.avlTree.removeNode(6)
      self.assertEqual(self.avlTree.printAllLevel(),"12,8,14,4,10,13,15")

   def test_removeNodeRightLeftCase(self):
      self.avlTree.insertNode(8)
      self.avlTree.insertNode(4)
      self.avlTree.insertNode(12)
      self.avlTree.insertNode(2)
      self.avlTree.insertNode(6)
      self.avlTree.insertNode(10)
      self.avlTree.insertNode(14)
      self.avlTree.insertNode(9)
      self.avlTree.insertNode(11)
      self.avlTree.removeNode(2)
      self.avlTree.removeNode(6)
      self.assertEqual(self.avlTree.printAllLevel(),"10,8,12,4,9,11,14")

   def test_recInsertNodeLeftLeftCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(7,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(5,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(1,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,6,1,5,7")

   def test_recInsertNodeLeftRightCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(7,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(1,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(3,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,6,1,3,7")

   def test_recInsertNodeRightRightCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(1,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(3,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(5,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,5,1,3,6")

   def test_recInsertNodeRightLeftCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(1,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(5,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(3,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"3,2,5,1,4,6")

   def test_recRemoveNodeLeftLeftCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(8,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(12,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(13,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(1,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(3,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(13,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"4,2,8,1,3,6,12")

   def test_recRemoveNodeLeftRightCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(8,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(12,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(13,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(5,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(7,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(13,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"6,4,8,2,5,7,12")

   def test_recRemoveNodeRightRightCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(8,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(12,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(14,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(13,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(15,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(6,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"12,8,14,4,10,13,15")

   def test_recRemoveNodeRightLeftCase(self):
      self.avlTree.root = self.avlTree.recInsertNode(8,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(4,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(12,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(6,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(10,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(14,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(9,self.avlTree.root)
      self.avlTree.root = self.avlTree.recInsertNode(11,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(2,self.avlTree.root)
      self.avlTree.root = self.avlTree.recRemoveNode(6,self.avlTree.root)
      self.assertEqual(self.avlTree.printAllLevel(),"10,8,12,4,9,11,14")

if __name__ == '__main__':
   print "AVLTree Testing"
   unittest.main()
