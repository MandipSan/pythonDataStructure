#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/04/2017

import unittest
from dataStructure.stack import *

class TestStack(unittest.TestCase):

   def setUp(self):
      self.stack = Stack()

   def test_push(self):
      self.stack.push(2)
      self.stack.push(1)
      self.assertEqual(self.stack.dumpList(),"1,2")

   def test_pop(self):
      self.stack.push(2)
      self.stack.push(1)
      self.stack.pop()
      self.assertEqual(self.stack.dumpList(),"2")

   def test_top(self):
      self.stack.push(2)
      self.stack.push(1)
      self.assertEqual(self.stack.top(),1)
            
   def test_isEmptyNot(self):
      self.stack.push(2)
      self.stack.push(1)
      self.assertEqual(self.stack.isEmpty(),False)

   def test_isEmpty(self):
      self.assertEqual(self.stack.isEmpty(),True)
   
   def test_getSizeOne(self):
      self.stack.push(2)
      self.assertEqual(self.stack.getSize(),1)

   def test_getSizeZero(self):
      self.assertEqual(self.stack.getSize(),0)

if __name__ == '__main__':
   print "Stack Testing"
   unittest.main()
