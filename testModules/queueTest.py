#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/04/2017

import unittest
from dataStructure.queue import *

class TestQueue(unittest.TestCase):

   def setUp(self):
      self.queue = Queue(3)
      
   def test_enqueue(self):
      self.queue.enqueue(1)
      self.queue.enqueue(2)
      self.queue.enqueue(3)
      self.assertEqual(self.queue.dumpQueue(),"1,2,3")

   def test_dequeue(self):
      self.queue.enqueue(1)
      self.queue.enqueue(2)
      self.queue.enqueue(3)
      self.queue.dequeue()
      self.assertEqual(self.queue.dumpQueue(),"2,3")

   def test_front(self):
      self.queue.enqueue(1)
      self.queue.enqueue(2)
      self.queue.enqueue(3)
      self.assertEqual(self.queue.front(),1)

   def test_isEmptyFalse(self):
      self.queue.enqueue(1)
      self.assertEqual(self.queue.isEmpty(),False)

   def test_isEmptyTrue(self):
      self.assertEqual(self.queue.isEmpty(),True)

   def test_getSizeZero(self):
      self.assertEqual(self.queue.getSize(),0)

   def test_getSizeOne(self):
      self.queue.enqueue(1)
      self.assertEqual(self.queue.getSize(),1)

   def test_arr_enqueue(self):
      self.queue.arrEnqueue(1)
      self.queue.arrEnqueue(2)
      self.assertEqual(self.queue.dumpArrQueue(),"1,2")

   def test_arr_dequeue(self):
      self.queue.arrEnqueue(1)
      self.queue.arrEnqueue(2)
      self.queue.arrEnqueue(3)
      self.queue.arrDequeue()
      self.assertEqual(self.queue.dumpArrQueue(),"2,3")
   
   def test_arr_enqueueOverLoop(self):
      self.queue.arrEnqueue(1)
      self.queue.arrEnqueue(2)
      self.queue.arrEnqueue(3)
      self.queue.arrDequeue()
      self.queue.arrEnqueue(4)
      self.assertEqual(self.queue.dumpArrQueue(),"2,3,4")

   def test_arr_front(self):
      self.queue.arrEnqueue(1)
      self.queue.arrEnqueue(2)
      self.assertEqual(self.queue.arrFront(),1)

   def test_arr_isFullFalse(self):
      self.assertEqual(self.queue.arrIsFull(),False)

   def test_arr_isFullTrue(self):
      self.queue.arrEnqueue(1)
      self.queue.arrEnqueue(2)
      self.queue.arrEnqueue(3)
      self.assertEqual(self.queue.arrIsFull(),True)

   def test_arr_isEmptyFalse(self):
      self.queue.arrEnqueue(1)
      self.assertEqual(self.queue.arrIsEmpty(),False)

   def test_arr_isEmptyTrue(self):
      self.assertEqual(self.queue.arrIsEmpty(),True)

   def test_arr_getSizeZero(self):
      self.assertEqual(self.queue.arrGetSize(),0)

   def test_arr_getSizeOne(self):
      self.queue.arrEnqueue(1)
      self.assertEqual(self.queue.arrGetSize(),1)


if __name__ == '__main__':
   print "Queue Testing"
   unittest.main()
