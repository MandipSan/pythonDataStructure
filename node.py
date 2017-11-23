#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   11/23/2017

class Node(object):

   #PURPOSE:   Set node's prevNode, nextNode and data to default values
   #INPUT:     data        - The data the node will hold
   #OUTPUT:    NONE
   def __init__(self, data):
      self.data = data
      self.prevNode = None
      self.nextNode = None

   #PURPOSE:   Sets the node's previous node 
   #INPUT:     prevNode    - The previous node to set as the node's prevNode
   #OUTPUT:    NONE
   def setPrevNode(self, prevNode):
      self.prevNode = prevNode

   #PURPOSE:   Sets the node's next node 
   #INPUT:     nextNode    - The next node to set as the node's nextNode
   #OUTPUT:    NONE
   def setNextNode(self, nextNode):
      self.nextNode = nextNode

   #PURPOSE:   Returns the node's data 
   #INPUT:     NONE
   #OUTPUT:    Returns the node's data
   def getData(self):
      return self.data

   #PURPOSE:   Returns the node's previous node
   #INPUT:     NONE
   #OUTPUT:    Returns the node's prevNode
   def getPrevNode(self):
      return self.prevNode

   #PURPOSE:   Returns the node's next node
   #INPUT:     NONE
   #OUTPUT:    Returns the node's nextNode
   def getNextNode(self):
      return self.nextNode

