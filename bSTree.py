#!/usr/bin/python

from treeNode import *
from stack import *

class BSTree(object):

   #PURPOSE:   Set the tree defualt values
   #INPUT:     NONE
   #OUTPUT:    NONE
   def __init__(self):
      self.root = None

   #PURPOSE:   Insert a node into the tree
   #INPUT:     data           - The data to insert into the tree
   #OUTPUT:    NONE
   def insertNode(self, data):
      if self.root == None:
         self.root = TreeNode(data)
      else:
        currentNode = self.root
        while currentNode != None:
           if currentNode.getData() > data:
              if currentNode.getLeftNode() != None:
                 currentNode = currentNode.getLeftNode()
              else:
                 newNode = TreeNode(data)
                 newNode.setParentNode(currentNode)
                 currentNode.setLeftNode(newNode)
                 break
           else: 
              if currentNode.getRightNode() != None:
                 currentNode = currentNode.getRightNode()
              else:
                 newNode = TreeNode(data)
                 newNode.setParentNode(currentNode)
                 currentNode.setRightNode(newNode)
                 break

   #PURPOSE:   Remove node of the given data from the tree 
   #INPUT:     data           - The data to be removed from the tree
   #OUTPUT:    NONE
#   def removeNode(self, data):

   #PURPOSE:   Find the node for the data given
   #INPUT:     data           - The data for the node to be found
   #OUTPUT:    Return node for the data given or None if not found
   def findNode(self, data):
      currentNode = self.root
      while currentNode != None:
         currentData = currentNode.getData()
         if currentData == data:
            return currentNode
         elif currentData > data:
            currentNode = currentNode.getLeftNode()
         elif currentData < data:
            currentNode = currentNode.getRightNode()
      return None

   #PURPOSE:   Find's the smallest node data from the startnode given
   #INPUT:     startNode      - The node to start searching from
   #OUTPUT:    Return the data for the smallest node
   def findSmallestNodeData(self, startNode):
      currentNode = startNode.getLeftNode()
      while currentNode != None:
         if currentNode.getLeftNode() == None:
            return currentNode.getData()
         currentNode = currentNode.getLeftNode()
      return startNode.getData()

   #PURPOSE:   Print's out tree in order(left, root, right)
   #INPUT:     NONE
   #OUTPUT:    NONE
   def printInOrder(self):
      printStack = Stack()
      currentNode = self.root.getLeftNode()
      if self.root != None:
         printStack.push(self.root)

      while not printStack.isEmpty() or currentNode != None:
         if currentNode != None:
            printStack.push(currentNode)
            currentNode = currentNode.getLeftNode()
         else:
            temp = printStack.top()
            printStack.pop()
            print temp.getData()
            currentNode = temp.getRightNode()

   #PURPOSE:   Print's out tree preorder(root, left, right)
   #INPUT:     NONE
   #OUTPUT:    NONE
   def printPreOrder(self):
      printStack = Stack()
      
      if self.root != None:
         print self.root.getData()
         if self.root.getRightNode() != None:
            printStack.push(self.root.getRightNode())
         if self.root.getLeftNode() != None:
            printStack.push(self.root.getLeftNode())

      while not printStack.isEmpty():
         currentNode = printStack.top()
         printStack.pop()
         print currentNode.getData()
         if currentNode.getRightNode() != None:
            printStack.push(currentNode.getRightNode())
         if currentNode.getLeftNode() != None:
            printStack.push(currentNode.getLeftNode())

   #PURPOSE:   Print's out tree post order(left, right, root)
   #INPUT:     NONE
   #OUTPUT:    NONE
   def printPostOrder(self):
      printStack = Stack()
      currentNode = None

      if self.root != None:
         if self.root.getRightNode() != None:
            printStack.push(self.root.getRightNode())
         printStack.push(self.root)
         currentNode = self.root.getLeftNode() 

      while not printStack.isEmpty():
         if currentNode == None:
            currentNode = printStack.top()
            printStack.pop()
            nodeCheck = printStack.top()
            if currentNode.getRightNode() == nodeCheck:
               printStack.pop()
               printStack.push(currentNode)
               if nodeCheck.getRightNode() != None:
                  printStack.push(nodeCheck.getRightNode())
               printStack.push(nodeCheck)
               currentNode = nodeCheck.getLeftNode()
            else:
               print currentNode.getData()
               currentNode = None
         else:
            if currentNode.getRightNode() != None:
               printStack.push(currentNode.getRightNode())
            printStack.push(currentNode)
            currentNode = currentNode.getLeftNode()


#****************************************************************************
#Recursive Version
#****************************************************************************

   #PURPOSE:   Insert a node into the tree
   #INPUT:     data           - The data to insert into the tree
   #           currentNode    - The node to check against
   #OUTPUT:    Return the current node
   def recInsertNode(self, data, currentNode):
      if currentNode == None:
         return TreeNode(data)
      else:
         if currentNode.getData() > data:
            currentNode.setLeftNode(self.recInsertNode(data, currentNode.getLeftNode()))
         else:
            currentNode.setRightNode(self.recInsertNode(data, currentNode.getRightNode()))
      return currentNode

   #PURPOSE:   Remove node of the given data from the tree 
   #INPUT:     data           - The data to be removed from the tree
   #OUTPUT:    NONE
   def recRemoveNode(self, data):
      rCurrentNode = self.recFindNode(data, self.root)
      if rCurrentNode == None:
         return
      #if node has both children
      if rCurrentNode.getLeftNode() != None and rCurrentNode.getRightNode() != None:
         cData = self.recFindSmallestNodeData(rCurrentNode.getRightNode())
         self.recRemoveNode(cData)
         rCurrentNode.setData(cData)
      #if node has child or right child only
      elif rCurrentNode.getLeftNode() != None or rCurrentNode.getRightNode() != None:
         tempPar = rCurrentNode.getParentNode()

         if rCurrentNode.getLeftNode() != None:
            tempChild = rCurrentNode.getLeftNode()
         else: 
            tempChild = rCurrentNode.getRightNode()

         tempChild.setParentNode(tempPar)
         
         if tempPar == None:
            self.root = tempChild
         else:
            if tempPar.getLeftNode() == rCurrentNode:
               tempPar.setLeftNode(tempChild)
            else:
               tempPar.setRightNode(tempChild)

         del rCurrentNode
      #if node has no children
      else:
         if rCurrentNode.getParentNode() == None:
            self.root = None
         else:
            if rCurrentNode.getParentNode().getLeftNode() == rCurrentNode:
               rCurrentNode.getParentNode().setLeftNode(None)
            else:
               rCurrentNode.getParentNode().setRightNode(None)

         del rCurrentNode
   
   #PURPOSE:   Find the node for the data given
   #INPUT:     data           - The data for the node to be found
   #           currentNode    - The current node to check against
   #OUTPUT:    Return node for the data given or None if not found
   def recFindNode(self, data, currentNode):
      if currentNode == None:
         return None
      elif currentNode.getData() > data:
         return self.recFindNode(data, currentNode.getLeftNode())
      elif currentNode.getData() < data:
         return self.recFindNode(data, currentNode.getRightNode())
      else:
         return currentNode

   #PURPOSE:   Find's the smallest node data from the startnode given
   #INPUT:     currentNode    - The node to start searching from
   #OUTPUT:    Return the data for the smallest node
   def recFindSmallestNodeData(self, currentNode):
      if currentNode.getLeftNode() == None:
         return currentNode.getData()
      else:
         return self.recFindSmallestNodeData(currentNode.getLeftNode())

   #PURPOSE:   Print's out tree in order(left, root, right)
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    NONE
   def recPrintInOrder(self, currentNode):
      if currentNode == None:
         return
      self.recPrintInOrder(currentNode.getLeftNode())  
      print currentNode.getData()
      self.recPrintInOrder(currentNode.getRightNode())

   #PURPOSE:   Print's out tree preorder(root, left, right)
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    NONE
   def recPrintPreOrder(self, currentNode):
      if currentNode == None:
         return
      print currentNode.getData()
      self.recPrintPreOrder(currentNode.getLeftNode())
      self.recPrintPreOrder(currentNode.getRightNode())

   #PURPOSE:   Print's out tree post order(left, right, root)
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    NONE
   def recPrintPostOrder(self,currentNode):
      if currentNode == None:
         return
      self.recPrintPostOrder(currentNode.getLeftNode())
      self.recPrintPostOrder(currentNode.getRightNode())
      print currentNode.getData() 

   #PURPOSE:   Print's the tree by it's levels starting from the root
   #INPUT:     NONE
   #OUTPUT:    NONE
   def recPrintAllLevel(self):
      for i in range(1, self.recGetHeight(self.root)+1):
         self.recPrintOneLevel(self.root, i)

   #PURPOSE:   Print's the level given from the node given when level equals one
   #INPUT:     currentNode    - The node to check if it is at level one
   #           level          - The current level 
   #OUTPUT:    NONE
   def recPrintOneLevel(self, currentNode, level):
      if currentNode == None:
         return
      if level == 1:
         print currentNode.getData()
      else:
         self.recPrintOneLevel(currentNode.getLeftNode(),level-1)
         self.recPrintOneLevel(currentNode.getRightNode(), level-1)
   
   #PURPOSE:   Return's the height of the tree
   #INPUT:     currentNode    - The current node to check
   #OUTPUT:    Return's the height of the tree
   def recGetHeight(self, currentNode):
      if currentNode == None:
         return 0; 
      else:
         lHeight = self.recGetHeight(currentNode.getLeftNode())
         rHeight = self.recGetHeight(currentNode.getRightNode())
         if lHeight > rHeight:
            return lHeight + 1
         else:
            return rHeight + 1
