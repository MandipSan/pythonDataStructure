#!/usr/bin/python

from node import *
from linkList import *

class Stack(LinkList):
   #PURPOSE:   Set default value for link list
   #INPUT:     NONE
   #OUTPUT:    NONE
   def __init__(self):
		super(Stack, self).__init__()

   #PURPOSE:   Push data to the top of the stack
   #INPUT:     data     - The to push onto the stack
   #OUTPUT:    NONE
   def push(self, data):
      super(Stack, self).addAtBeginning(data)

   #PURPOSE:   Pop's the top of the stack
   #INPUT:     NONE
   #OUTPUT:    NONE
   def pop(self):
      super(Stack, self).removeAtBeginning()
   
   #PURPOSE:   Get the data for the top of the stack
   #INPUT:     NONE
   #OUTPUT:    Return's the data at the top of the stack
   def top(self):
      return super(Stack, self).findNthNode(0)

   #PURPOSE:   Checks if the stack is empty
   #INPUT:     NONE
   #OUTPUT:    Return's true if the stack isn't empty
   def isEmpty(self):
      return super(Stack, self).count() == 0

   #PURPOSE:   Gets the size of the stack
   #INPUT:     NONE
   #OUTPUT:    Return's the number of items in the stack
   def getSize(self):
      return super(Stack, self).count()
