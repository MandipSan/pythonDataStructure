#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   11/29/2017

#****************************************************************************
#NOTE:
#Methods for the same implementation version must be used for correct results
#Mixing version method can result in error or other problems
#**************************************************************************** 

from linkList import *

class Queue(object):

   #PURPOSE:   Set the queue to the default values
   #INPUT:     queueArrSize   - The queue cirular array needs to be(set 5 as default)
   #OUTPUT:    NONE
   def __init__(self, queueArrSize = 5):
      self.queueList = LinkList()
      self.queueArrFront = -1
      self.queueArrEnd = 0
      self.queueArrSize = queueArrSize
      self.queueArrCurSize = 0
      #initializes the array to the size
      self.queueArr = [0 for i in range(queueArrSize)] 

#***********************************************************************
#Queue use link list version
#***********************************************************************

   #PURPOSE:   Enqueue's data to end of the queue 
   #INPUT:     data           - The data to add to the queue
   #OUTPUT:    NONE
   def enqueue(self, data):
      self.queueList.addAtEnd(data)

   #PURPOSE:   Dequeue's data from the front of the queue 
   #INPUT:     NONE
   #OUTPUT:    NONE
   def dequeue(self):
      self.queueList.removeAtBeginning()

   #PURPOSE:   Return's the data from the first item in the queue
   #INPUT:     NONE
   #OUTPUT:    Return the data of first item
   def front(self):
      return self.queueList.findNthNode(0)

   #PURPOSE:   Checks if queue is empty 
   #INPUT:     NONE
   #OUTPUT:    Return's boolean of whether queue is empty
   def isEmpty(self):
      return (self.queueList.count() == 0)

   #PURPOSE:   Return the size of the queue 
   #INPUT:     NONE
   #OUTPUT:    Return integer of the current size of the queue
   def getSize(self):
      return self.queueList.count()

   #PURPOSE:   Dump the queue for testing 
   #INPUT:     NONE
   #OUTPUT:    Return a string of the data separated by , 
   def dumpQueue(self):
      return self.queueList.dumpList()

#***********************************************************************
#Queue use circular array version
#***********************************************************************

   #PURPOSE:   Enqueue's data to end of the queue 
   #INPUT:     data           - The data to add to the queue
   #OUTPUT:    NONE
   def arrEnqueue(self, data):
      if not self.arrIsFull():
         self.queueArr[self.queueArrEnd] = data
         self.queueArrCurSize += 1
         if self.queueArrFront == -1:
            self.queueArrFront = self.queueArrEnd
         tempEnd = 0
         if self.queueArrEnd + 1 < self.queueArrSize:
            tempEnd = self.queueArrEnd + 1
         self.queueArrEnd = tempEnd

   #PURPOSE:   Dequeue's data from the front of the queue 
   #INPUT:     NONE
   #OUTPUT:    NONE
   def arrDequeue(self):
      if not self.arrIsEmpty():
         if self.queueArrFront + 1 < self.queueArrSize:
            self.queueArrFront = self.queueArrFront + 1
            self.queueArrCurSize -= 1
         else:
            self.queueArrFront = 0
         if self.queueArrFront == self.queueArrEnd:
            self.queueArrFront = -1

   #PURPOSE:   Return's the data from the first item in the queue
   #INPUT:     NONE
   #OUTPUT:    Return the data of first item
   def arrFront(self):
      return self.queueArr[self.queueArrFront] if not self.arrIsEmpty() else None

   #PURPOSE:   Checks if queue is full 
   #INPUT:     NONE
   #OUTPUT:    Return's boolean of whether queue is full
   def arrIsFull(self):
      return (self.queueArrFront == self.queueArrEnd)

   #PURPOSE:   Checks if queue is empty 
   #INPUT:     NONE
   #OUTPUT:    Return's boolean of whether queue is empty
   def arrIsEmpty(self):
      return (self.queueArrFront == -1)

   #PURPOSE:   Return the size of the queue 
   #INPUT:     NONE
   #OUTPUT:    Return integer of the current size of the queue
   def arrGetSize(self):
      return self.queueArrCurSize

   #PURPOSE:   Dump the queue for testing 
   #INPUT:     NONE
   #OUTPUT:    Return a string of the data separated by , 
   def dumpArrQueue(self):
      output = str(self.queueArr[self.queueArrFront])
      i = self.queueArrFront + 1
      if i >= self.queueArrSize:
         i = 0
      while i != self.queueArrEnd and i != -1:
         output = output + "," + str(self.queueArr[i])
         i += 1
         if i >= self.queueArrSize:
            i = 0
      return output
