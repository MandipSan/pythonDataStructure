#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   11/23/2017

from node import *

class TreeNode(Node):

   #PURPOSE:   Set node's value to default values
   #INPUT:     data        - The data the node will hold
   #OUTPUT:    NONE
   def __init__(self, data):
      super(TreeNode, self).__init__(data)
      self.parentNode = None

   #PURPOSE:   Set the node's parent node
   #INPUT:     parentNode  - The parent node to set as the node's parent node 
   #OUTPUT:    NONE 
   def setParentNode(self, parentNode):
      self.parentNode = parentNode

   #PURPOSE:   Set the node's right node
   #INPUT:     rightNode   - The right node to set as the node's right node  
   #OUTPUT:    NONE 
   def setRightNode(self, rightNode):
      super(TreeNode, self).setNextNode(rightNode)

   #PURPOSE:   Set the node's left node
   #INPUT:     leftNode    - The left node to set as the node's left node  
   #OUTPUT:    NONE 
   def setLeftNode(self, leftNode):
      super(TreeNode, self).setPrevNode(leftNode)

   #PURPOSE:   Set the node's data
   #INPUT:     data        - The data to reset the data to   
   #OUTPUT:    NONE 
   def setData(self, data):
      self.data = data

   #PURPOSE:   Returns the node's parent node
   #INPUT:     NONE
   #OUTPUT:    Returns the node's parent node
   def getParentNode(self):
      return self.parentNode

   #PURPOSE:   Returns the node's right node
   #INPUT:     NONE  
   #OUTPUT:    Returns the node's right node  
   def getRightNode(self):
      return super(TreeNode, self).getNextNode()

   #PURPOSE:   Returns the node's left node
   #INPUT:     NONE  
   #OUTPUT:    Returns the node's left node  
   def getLeftNode(self):
      return super(TreeNode, self).getPrevNode()

