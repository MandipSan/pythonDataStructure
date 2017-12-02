#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   11/28/2017

from bSTree import *

class AVLTree(BSTree):

   #PURPOSE:   Set the tree defualt values
   #INPUT:     NONE
   #OUTPUT:    NONE
   def __init__(self):
      self.root = None

   #PURPOSE:   Rotates the node given to the left
   #INPUT:     currentNode    - The node to rotate
   #OUTPUT:    Return the new node that is now in the position of the given currentNode
   def rotateLeft(self, currentNode):
      if currentNode == None:
         return None
        
      curRight = currentNode.getRightNode()
      curRightLeft = curRight.getLeftNode()

      currentNode.setRightNode(curRightLeft)
      curRight.setLeftNode(currentNode)
      
      return curRight 

   #PURPOSE:   Rotates the node given to the right
   #INPUT:     currentNode    - The node to rotate
   #OUTPUT:    Return the new node that is now in the position of the given currentNode
   def rotateRight(self, currentNode):
      if currentNode == None:
         return None

      curLeft = currentNode.getLeftNode()
      curLeftRight = curLeft.getRightNode()

      currentNode.setLeftNode(curLeftRight)
      curLeft.setRightNode(currentNode)

      return curLeft

   #PURPOSE:   Checks if the sub tree is balanced
   #INPUT:     currentNode    - The node to check sub tree from
   #OUTPUT:    Returns true if balanced else false
   def isSubTreeBalanced(self, currentNode):
      if currentNode == None:
         return True
      lH = 0
      rH = 0 
      if currentNode.getLeftNode() != None:
         lH = super(AVLTree, self).getHeight(currentNode.getLeftNode()) 
      if currentNode.getRightNode() != None:
         rH =  super(AVLTree, self).getHeight(currentNode.getRightNode())
      curBalance = lH - rH
      if curBalance < -1 or curBalance > 1:
         return False
      return True

#****************************************************************************
#Non Recursive Version of Methods
#****************************************************************************

   #PURPOSE:   Insert's the data into the tree and checks if it is balanced if not then balance the tree
   #INPUT:     data           - The data to add to the tree
   #OUTPUT:    NONE
   def insertNode(self, data):
      super(AVLTree, self).insertNode(data)

      currentNode = None
      parCurNode = None
      if not self.isSubTreeBalanced(self.root):
         if not self.isSubTreeBalanced(self.root.getLeftNode()):
            parCurNode = self.root
            currentNode = self.root.getLeftNode()
         elif not self.isSubTreeBalanced(self.root.getRightNode()):
            parCurNode = self.root
            currentNode = self.root.getRightNode()
         else:
            currentNode = self.root

      while currentNode != None:
         #To move to the node that is one level above the unbalances
         if not self.isSubTreeBalanced(currentNode.getLeftNode()):
            parCurNode = currentNode
            currentNode = currentNode.getLeftNode()
         elif not self.isSubTreeBalanced(currentNode.getRightNode()):
            parCurNode = currentNode
            currentNode = currentNode.getRightNode()
         #Rebalances the tree 
         else:
            tempNode = None
            curBalance = super(AVLTree, self).getHeight(currentNode.getLeftNode()) - super(AVLTree, self).getHeight(currentNode.getRightNode())
         
            #Check if it a Left unbalance
            if curBalance > 1:
               #If left right case 
               if currentNode.getLeftNode().getData() < data:
                  currentNode.setLeftNode(self.rotateLeft(currentNode.getLeftNode()))
               tempNode = self.rotateRight(currentNode)
            #Right unbalance
            elif curBalance < -1:
               #If right left case
               if currentNode.getRightNode().getData() > data:
                  currentNode.setRightNode(self.rotateRight(currentNode.getRightNode()))
               tempNode = self.rotateLeft(currentNode)
         
            #Sets the parent node to be the correct rotated node or set the new root if old root was rotated
            if parCurNode != None:
               if parCurNode.getLeftNode() == currentNode:
                  parCurNode.setLeftNode(tempNode)
               elif parCurNode.getRightNode() == currentNode:
                  parCurNode.setRightNode(tempNode)
               break;
            else:
               self.root = tempNode
               break;

   def removeNode(self, data):
      super(AVLTree, self).removeNode(data)
      
      currentNode = None
      parCurNode = None
      if not self.isSubTreeBalanced(self.root):
         if not self.isSubTreeBalanced(self.root.getLeftNode()):
            parCurNode = self.root
            currentNode = self.root.getLeftNode()
         elif not self.isSubTreeBalanced(self.root.getRightNode()):
            parCurNode = self.root
            currentNode = self.root.getRightNode()
         else:
            currentNode = self.root

      while currentNode != None:
         #To move to the node that is one level above the unbalances
         if not self.isSubTreeBalanced(currentNode.getLeftNode()):
            parCurNode = currentNode
            currentNode = currentNode.getLeftNode()
         elif not self.isSubTreeBalanced(currentNode.getRightNode()):
            parCurNode = currentNode
            currentNode = currentNode.getRightNode()
         #Rebalances the tree 
         else:
            tempNode = None
            curBalance = super(AVLTree, self).getHeight(currentNode.getLeftNode()) - super(AVLTree, self).getHeight(currentNode.getRightNode())
            curLBalance = 0
            curRBalance = 0
            if currentNode.getLeftNode() != None:
               curLBalance = super(AVLTree, self).recGetHeight(currentNode.getLeftNode().getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getLeftNode().getRightNode())
            if currentNode.getRightNode() != None:
               curRBalance = super(AVLTree, self).recGetHeight(currentNode.getRightNode().getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getRightNode().getRightNode())

            #Check if it a Left unbalance
            if curBalance > 1:
               #If left right case 
               if curLBalance < 0:
                  currentNode.setLeftNode(self.rotateLeft(currentNode.getLeftNode()))
               tempNode = self.rotateRight(currentNode)
            #Right unbalance
            elif curBalance < -1:
               #If right left case
               if curRBalance > 0:
                  currentNode.setRightNode(self.rotateRight(currentNode.getRightNode()))
               tempNode = self.rotateLeft(currentNode)
         
            #Sets the parent node to be the correct rotated node or set the new root if old root was rotated
            if parCurNode != None:
               if parCurNode.getLeftNode() == currentNode:
                  parCurNode.setLeftNode(tempNode)
               elif parCurNode.getRightNode() == currentNode:
                  parCurNode.setRightNode(tempNode)
               break;
            else:
               self.root = tempNode
               break;
     
#****************************************************************************
#Recursive Version of Methods
#****************************************************************************

   #PURPOSE:   Insert's the data into the tree and checks if it is balanced if not then balance the tree
   #INPUT:     data           - The data to add to the tree
   #           currentNode    - The current node to start looking for an insertion point after
   #OUTPUT:    Returns the node worked on
   def recInsertNode(self, data, currentNode):
      if currentNode == None:
         return TreeNode(data)
      else:
         if currentNode.getData() > data:
            currentNode.setLeftNode(self.recInsertNode(data, currentNode.getLeftNode()))
         elif currentNode.getData() < data:
            currentNode.setRightNode(self.recInsertNode(data, currentNode.getRightNode()))
         else:
            return currentNode

      curBalance = super(AVLTree, self).recGetHeight(currentNode.getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getRightNode())

      #Check if it a Left unbalance
      if curBalance > 1:
         #If left right case 
         if currentNode.getLeftNode().getData() < data:
            currentNode.setLeftNode(rotateLeft(currentNode.getLeftNode()))

         return self.rotateRight(currentNode)
      #Right unbalance
      elif curBalance < -1:
         #If right left case
         if currentNode.getRightNode().getData() > data:
            currentNode.setRightNode(self.rotateRight(currentNode.getRightNode()))

         return self.rotateLeft(currentNode)

      return currentNode

   #PURPOSE:   Removes the given data from the tree and make sure the tree is still balanced
   #INPUT:     data           - The data to remove from the tree
   #           currentNode    - The node check if it match the data
   #OUTPUT:    Return's the updated node 
   def recRemoveNode(self, data, currentNode):
      if currentNode == None:
         return None
      else:
         if currentNode.getData() > data:
            currentNode.setLeftNode(self.recRemoveNode(data,currentNode.getLeftNode()))
         elif currentNode.getData() < data:
            currentNode.setRightNode(self.recRemoveNode(data,currentNode.getRightNode()))
         else:
            if currentNode.getLeftNode() != None and currentNode.getRightNode() != None:
               tempData = super(AVLTree, self).recFindSmallestNodeData(currentNode.getRightNode())
               currentNode.setRightNode(recRemoveNode(tempData, currentNode.getRightNode()))
               currentNode.setData(tempData)
            elif currentNode.getLeftNode() != None or currentNode.getRightNode() != None:
               tempChild = None
               if currentNode.getLeftNode() != None:
                  tempChild = currentNode.getLeftNode()
               elif currentNode.getRightNode() != None:
                  tempChild = currentNode.getRightNode()
               del currentNode
               currentNode = tempChild
            else:
               del currentNode
               return None
         
         curBalance = super(AVLTree, self).recGetHeight(currentNode.getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getRightNode())
         curLBalance = 0
         curRBalance = 0
         if currentNode.getLeftNode() != None:
            curLBalance = super(AVLTree, self).recGetHeight(currentNode.getLeftNode().getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getLeftNode().getRightNode())
         if currentNode.getRightNode() != None:
            curRBalance = super(AVLTree, self).recGetHeight(currentNode.getRightNode().getLeftNode()) - super(AVLTree, self).recGetHeight(currentNode.getRightNode().getRightNode())
                     
         #Check if it a Left unbalance
         if curBalance > 1:
            #If left right case 
            if curLBalance < 0:
               currentNode.setLeftNode(rotateLeft(currentNode.getLeftNode()))
            currentNode = self.rotateRight(currentNode)
         #Right unbalance
         elif curBalance < -1:
            #If right left case
            if curRBalance > 0:
               currentNode.setRightNode(self.rotateRight(currentNode.getRightNode()))
            currentNode = self.rotateLeft(currentNode)

         return currentNode
