#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/01/2017

#****************************************************************************
#NOTE:
#The left and right node comparison for greater than and lesser than is for
# number values. Uses of other types of values can cause known results
#Duplicate data is allowed
#**************************************************************************** 

from treeNode import *
from stack import *
from queue import *

class BSTree(object):

   #PURPOSE:   Set the tree defualt values
   #INPUT:     NONE
   #OUTPUT:    NONE
   def __init__(self):
      self.root = None

#****************************************************************************
#Non Recursive Version of Methods
#****************************************************************************

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
                 currentNode.setLeftNode(newNode)
                 break
           else: 
              if currentNode.getRightNode() != None:
                 currentNode = currentNode.getRightNode()
              else:
                 newNode = TreeNode(data)
                 currentNode.setRightNode(newNode)
                 break

   #PURPOSE:   Remove node of the given data from the tree 
   #INPUT:     data           - The data to be removed from the tree
   #OUTPUT:    NONE
   def removeNode(self, data):
      currentNode = self.root
      tempPar = None

      while currentNode != None:
         if currentNode.getData() > data:
            tempPar = currentNode
            currentNode = currentNode.getLeftNode()
         elif currentNode.getData() < data:
            tempPar = currentNode
            currentNode = currentNode.getRightNode()
         else:
            if currentNode.getLeftNode() != None and currentNode.getRightNode() != None:
               temp = currentNode.getRightNode()
               tempP = currentNode
               dataTemp = None
               while temp != None:
                  if temp.getLeftNode() == None:
                     if temp == currentNode.getRightNode():
                        currentNode.setRightNode(None)
                     else:
                        tempP.setLeftNode(None)
                     dataTemp = temp.getData()
                     del temp
                     temp = None
                  else:
                     tempP = temp
                     temp = temp.getLeftNode()
               currentNode.setData(dataTemp)
               return
            elif currentNode.getLeftNode() != None or currentNode.getRightNode() != None:
               tempChild = None
               if currentNode.getLeftNode() != None:
                  tempChild = currentNode.getLeftNode()
               elif currentNode.getRightNode() != None:
                  tempChild = currentNode.getRightNode()
               if tempPar != None:
                  if tempPar.getLeftNode() == currentNode:
                     tempPar.setLeftNode(tempChild)
                  else:
                     tempPar.setRightNode(tempChild)
               else:
                  self.root = tempChild
            else:
               if tempPar != None:
                  if tempPar.getLeftNode() == currentNode:
                     tempPar.setLeftNode(None)
                  else:
                     tempPar.setRightNode(None)
               else:
                  self.root = None
            del currentNode
            currentNode = None

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

   #PURPOSE:   Print's out tree in order(left, root, right) to a string
   #INPUT:     NONE
   #OUTPUT:    Return a string of the print out
   def printInOrder(self):
      output = ""
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
            if output == "":
               output = str(temp.getData())
            else:
               output = output + "," + str(temp.getData())
            currentNode = temp.getRightNode()
      return output

   #PURPOSE:   Print's out tree preorder(root, left, right) to a string
   #INPUT:     NONE
   #OUTPUT:    Return a string of the print out
   def printPreOrder(self):
      output = ""
      printStack = Stack()
      
      if self.root != None:
         output = str(self.root.getData())
         if self.root.getRightNode() != None:
            printStack.push(self.root.getRightNode())
         if self.root.getLeftNode() != None:
            printStack.push(self.root.getLeftNode())

      while not printStack.isEmpty():
         currentNode = printStack.top()
         printStack.pop()
         output = output + "," + str(currentNode.getData())
         if currentNode.getRightNode() != None:
            printStack.push(currentNode.getRightNode())
         if currentNode.getLeftNode() != None:
            printStack.push(currentNode.getLeftNode())
      return output

   #PURPOSE:   Print's out tree post order(left, right, root) to a string
   #INPUT:     NONE
   #OUTPUT:    Return a string of the print out
   def printPostOrder(self):
      output = ""
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
               if output == "":
                  output = str(currentNode.getData())
               else:
                  output = output + "," + str(currentNode.getData())
               currentNode = None
         else:
            if currentNode.getRightNode() != None:
               printStack.push(currentNode.getRightNode())
            printStack.push(currentNode)
            currentNode = currentNode.getLeftNode()
      return output

   #PURPOSE:   Print's the tree by it's levels starting from the root(breadth first) to a string
   #INPUT:     NONE
   #OUTPUT:    Return a string of the print out
   def printAllLevel(self):
      output = ""
      tempQue = Queue()
      tempQue.enqueue(self.root)
      while not tempQue.isEmpty():
         currentNode = tempQue.front()
         tempQue.dequeue()
         if output == "":
            output = str(currentNode.getData())
         else:
            output = output + "," + str(currentNode.getData())
         if currentNode.getLeftNode() != None:
            tempQue.enqueue(currentNode.getLeftNode())
         if currentNode.getRightNode() != None:
            tempQue.enqueue(currentNode.getRightNode())
      return output
  
   #PURPOSE:   Print's the level given from the node given when level equals one(breadth first)
   #              to a string
   #INPUT:     level          - The current level 
   #OUTPUT:    Return a string of the print out
   def printOneLevel(self, level):
      output = ""
      curLevel = 1
      numOfNodeAtCurLvl = 1
      numOfNodeAtNextLvl = 0
      tempQue = Queue()
      tempQue.enqueue(self.root)
      while not tempQue.isEmpty():
         currentNode = tempQue.front()
         tempQue.dequeue()
         numOfNodeAtCurLvl -= 1
         if curLevel != level:
            if currentNode.getLeftNode() != None:
               tempQue.enqueue(currentNode.getLeftNode())
               numOfNodeAtNextLvl += 1
            if currentNode.getRightNode() != None:
               tempQue.enqueue(currentNode.getRightNode())
               numOfNodeAtNextLvl += 1
            if numOfNodeAtCurLvl == 0:
               numOfNodeAtCurLvl = numOfNodeAtNextLvl
               numOfNodeAtNextLvl = 0
               curLevel += 1
         else:
            if output == "":
               output = str(currentNode.getData())
            else:
               output = output + "," + str(currentNode.getData())
      return output

   #PURPOSE:   Return's the height of the tree from the given start node
   #INPUT:     currentNode    - The node start the height from
   #OUTPUT:    Return's the height of the tree
   def getHeight(self, currentNode):
      curLevel = 0
      numOfNodeAtCurLvl = 1
      numOfNodeAtNextLvl = 0
      tempQue = Queue()
      if currentNode != None:
         tempQue.enqueue(currentNode)
      while not tempQue.isEmpty():
         currNode = tempQue.front()
         tempQue.dequeue()
         numOfNodeAtCurLvl -= 1
         if currNode.getLeftNode() != None:
            tempQue.enqueue(currNode.getLeftNode())
            numOfNodeAtNextLvl += 1
         if currNode.getRightNode() != None:
            tempQue.enqueue(currNode.getRightNode())
            numOfNodeAtNextLvl += 1
         if numOfNodeAtCurLvl == 0:
            numOfNodeAtCurLvl = numOfNodeAtNextLvl
            numOfNodeAtNextLvl = 0
            curLevel += 1
      return curLevel

#****************************************************************************
#Recursive Version of Methods
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
   #           currentNode    - The node to check
   #OUTPUT:    NONE
   def recRemoveNode(self, data, currentNode):
      if currentNode == None:
         return None
         
      if currentNode.getData() > data:
         currentNode.setLeftNode(self.recRemoveNode(data, currentNode.getLeftNode())) 
      elif currentNode.getData() < data:
         currentNode.setRightNode(self.recRemoveNode(data, currentNode.getRightNode()))
      else:
         #if node has both children
         if currentNode.getLeftNode() != None and currentNode.getRightNode() != None:
            cData = self.recFindSmallestNodeData(currentNode.getRightNode())
            currentNode.setRightNode(self.recRemoveNode(cData, currentNode.getRightNode()))
            currentNode.setData(cData)
         #if node has left child or right child only
         elif currentNode.getLeftNode() != None or currentNode.getRightNode() != None:
            if currentNode.getLeftNode() != None:
               tempChild = currentNode.getLeftNode()
            else: 
               tempChild = currentNode.getRightNode()
            del currentNode
            return tempChild
         #if node has no children
         else:
            del currentNode
            return None
      return currentNode
   
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

   #PURPOSE:   Print's out tree in order(left, root, right) to a string
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    Return a string of the print out
   def recPrintInOrder(self, currentNode):
      output = ""
      if currentNode == None:
         return output
      outputLeft = str(self.recPrintInOrder(currentNode.getLeftNode()))
      outputRoot = str(currentNode.getData())
      outputRight = str(self.recPrintInOrder(currentNode.getRightNode()))
      if outputLeft != "": output = outputLeft
      if outputRoot != "": output = output + "," + outputRoot if output != "" else outputRoot
      if outputRight != "": output = output + "," + outputRight if output != "" else outputRight
      return output

   #PURPOSE:   Print's out tree preorder(root, left, right) to a string
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    Return a string of the print out 
   def recPrintPreOrder(self, currentNode):
      output = ""
      if currentNode == None:
         return output
      outputRoot = str(currentNode.getData())
      outputLeft = str(self.recPrintPreOrder(currentNode.getLeftNode()))
      outputRight = str(self.recPrintPreOrder(currentNode.getRightNode()))
      if outputRoot != "": output = outputRoot
      if outputLeft != "": output = output + "," + outputLeft if output != "" else outputLeft
      if outputRight != "": output = output + "," + outputRight if output != "" else outputRight
      return output

   #PURPOSE:   Print's out tree post order(left, right, root) to a string
   #INPUT:     currentNode    - The current node to check to print
   #OUTPUT:    Return a string of the print out
   def recPrintPostOrder(self,currentNode):
      output = ""
      if currentNode == None:
         return output
      outputLeft = str(self.recPrintPostOrder(currentNode.getLeftNode()))
      outputRight = str(self.recPrintPostOrder(currentNode.getRightNode()))
      outputRoot = str(currentNode.getData())
      if outputLeft != "": output = outputLeft
      if outputRight != "": output = output + "," + outputRight if output != "" else outputRight
      if outputRoot != "": output = output + "," + outputRoot if output != "" else outputRoot
      return output

   #PURPOSE:   Print's the tree by it's levels starting from the root(breadth first) to a string
   #INPUT:     NONE
   #OUTPUT:    Return a string of the print out
   def recPrintAllLevel(self):
      output = ""
      for i in range(1, self.recGetHeight(self.root)+1):
            output = str(self.recPrintOneLevel(self.root, i)) if output == "" else output + "," + str(self.recPrintOneLevel(self.root, i))
      return output

   #PURPOSE:   Print's the level given from the node given when level equals one to a string
   #INPUT:     currentNode    - The node to check if it is at level one
   #           level          - The current level 
   #OUTPUT:    Reutrn a string of the print out
   def recPrintOneLevel(self, currentNode, level):
      output = ""
      outputLeft = ""
      outputRight = ""
      if currentNode == None:
         return output
      if level == 1:
         output = str(currentNode.getData())
      else:
         outputLeft = str(self.recPrintOneLevel(currentNode.getLeftNode(),level-1))
         outputRight = str(self.recPrintOneLevel(currentNode.getRightNode(), level-1))
      if outputLeft != "": output = output + "," + outputLeft if output != "" else outputLeft
      if outputRight != "": output = output + "," + outputRight if output != "" else outputRight
      return output
   
   #PURPOSE:   Return's the height of the tree from the given start node
   #INPUT:     currentNode    - The node to start checking the height from
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
