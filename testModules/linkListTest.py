#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/04/2017

import unittest
from dataStructure.linkList import *

class TestLinkList(unittest.TestCase):

   def setUp(self):
      self.list = LinkList()
      self.list.addAtBeginning(3)
      self.list.addAtBeginning(2)
      self.list.addAtBeginning(1)
      
   def tearDown(self):
      self.list = None

   def test_addAtBeginning(self):
      self.assertEqual(self.list.dumpList(),"1,2,3")

   def test_removeAtBeginning(self):
      self.list.removeAtBeginning()
      self.assertEqual(self.list.dumpList(),"2,3")

   def test_addAtEnd(self):
      self.list.addAtEnd(4)
      self.assertEqual(self.list.dumpList(),"1,2,3,4")

   def test_removeAtEnd(self):
      self.list.removeAtEnd()
      self.assertEqual(self.list.dumpList(),"1,2")

   def test_addAfter(self):
      self.list.addAtAfter(5,2)
      self.assertEqual(self.list.dumpList(),"1,2,5,3")

   def test_removeAt(self):
      self.list.removeAt(2)
      self.assertEqual(self.list.dumpList(),"1,3")

   def test_findNthNode(self):
      self.assertEqual(self.list.findNthNode(2),3)

   def test_findListMiddleOdd(self):
      self.assertEqual(self.list.findListMiddle(),2)

   def test_findListMiddleEven(self):
      self.list.addAtBeginning(0)
      self.assertEqual(self.list.findListMiddle(),3)   

   def test_count(self):
      self.assertEqual(self.list.count(),3)

if __name__ == '__main__':
   print "Link List Testing"
   unittest.main()
