#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   11/23/2017

from node import *

class LinkList(object):

   #PURPOSE:   Set the head and end to default value of None
   #INPUT:     NONE
   #OUTPUT:    NONE
   def __init__(self):
      self.head = None
      self.end = None

   #PURPOSE:   Adds a node to the end of the list
   #INPUT:     data        - The data to add to the new node
   #OUTPUT:    NONE
   def addAtEnd(self, data):
      temp = Node(data)
      if self.end == None:      
         self.head = temp
         self.end = temp
      else:
         self.end.setNextNode(temp)
         temp.setPrevNode(self.end)
         self.end = temp

   #PURPOSE:   Adds a node to the beginning of the list
   #INPUT:     data        - The data to add to the new node
   #OUTPUT:    NONE
   def addAtBeginning(self, data):
      temp = Node(data)
      if self.head == None:
         self.end = temp
         self.head = temp
      else:
         self.head.setPrevNode(temp)
         temp.setNextNode(self.head)
         self.head = temp

   #PURPOSE:   Adds a node after a given node
   #INPUT:     data        - The data to add to the new node
   #           afterData   - The data for the node to place the new node after
   #OUTPUT:    NONE
   def addAtAfter(self, data, afterData):
      foundNode = self.searchNode(afterData)
      if self.end == foundNode or foundNode == None:
         self.addAtEnd(data)
      else:
         temp = Node(data)
         temp.setNextNode(foundNode.getNextNode())
         temp.setPrevNode(foundNode)
         foundNode.getNextNode().setPrevNode(temp)
         foundNode.setNextNode(temp)

   #PURPOSE:   Finds and returns node 
   #INPUT:     data     - The data for the node to be found
   #OUTPUT:    Returns the node if found else returns None
   def searchNode(self, data):
      temp = self.head
      while temp != None:
         if temp.getData() == data:
            return temp;
         temp = temp.getNextNode();
      return None

   #PURPOSE:   Finds the data for the node in the position given
   #INPUT:     nth      - The node position to get the data
   #OUTPUT:    Returns the data for the node at the given position else return None
   def findNthNode(self, nth):
      temp = self.head
      pos = 0
      while temp != None:
         if pos == nth:
            return temp.getData();
         pos += 1
         temp = temp.getNextNode();
      return None

   #PURPOSE:   Counts the number of nodes in the list and return amount
   #INPUT:     NONE
   #OUTPUT:    Returns number of node in the list
   def count(self):
      temp = self.head
      pos = 0
      while temp != None:
         pos += 1
         temp = temp.getNextNode();
      return pos

   #PURPOSE:   Finds the data for the middle of the list
   #INPUT:     NONE
   #OUTPUT:    Returns the data for the middle of the list else return None
   def findListMiddle(self):
      temp = self.head
      count  = self.count()/2
      pos = 0
      if count % 2 == 0:
         count += 1
      while temp != None:
         if pos == count:
            return temp.getData();
         pos += 1
         temp = temp.getNextNode();
      return None

   #PURPOSE:   Removes node at the end of the list
   #INPUT:     NONE
   #OUTPUT:    NONE
   def removeAtEnd(self):
      if self.end != None:
         if self.end.getPrevNode() == None:
            del self.end
            self.end = None
            self.head = None
         else:
            temp = self.end
            self.end = self.end.getPrevNode()
            self.end.setNextNode(None)
            del temp

   #PURPOSE:   Removes node at the beginning of the list
   #INPUT:     NONE
   #OUTPUT:    NONE
   def removeAtBeginning(self):
      if self.head != None:
         if self.head.getNextNode() == None:
            del self.head
            self.head = None
            self.end = None
         else:
            temp = self.head
            self.head = self.head.getNextNode()
            self.head.setPrevNode(None)
            del temp

   #PURPOSE:   Removes node for given data
   #INPUT:     data     - The data for the node to be removed 
   #OUTPUT:    NONE
   def removeAt(self, data):
      foundNode = self.searchNode(data)
      if foundNode != None:
         temp = foundNode.getPrevNode()
         temp.setNextNode(foundNode.getNextNode())
         temp = foundNode.getNextNode()
         temp.setPrevNode(foundNode.getPrevNode())
         del foundNode 

   #PURPOSE:   Dump the list for testing
   #INPUT:     NONE
   #OUTPUT:    NONE
   def dumpList(self):
      temp = self.head
      while temp != None:
         print temp.getData()
         print "->"
         temp = temp.getNextNode();
