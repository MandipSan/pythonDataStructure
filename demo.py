#!/usr/bin/python

#Created By:      Mandip Sangha
#Last Modified:   12/05/2017

import sys
from dataStructure import linkList
from dataStructure import stack
from dataStructure import queue
from dataStructure import bSTree
from dataStructure import aVLTree

#PURPOSE:   Runs demo for linklist
#INPUT:     NONE
#OUTPUT:    NONE
def runLinkList():
   run = True
   myLinkList = linkList.LinkList()
   command = { "IB" : myLinkList.addAtBeginning,
               "IE" : myLinkList.addAtEnd,
               "IA" : myLinkList.addAtAfter,
               "RB" : myLinkList.removeAtBeginning,
               "RE" : myLinkList.removeAtEnd,
               "RA" : myLinkList.removeAt,
               "F"  : myLinkList.findNthNode,
               "C"  : myLinkList.count,
               "FM" : myLinkList.findListMiddle,
               "P"  : myLinkList.printList
   }

   while run:
      inData = raw_input("Enter Command(H - for Help): ")
      inData = inData.replace(" ", "")
      inData = inData.upper() 

      if inData in command:
         output = ""
         if inData == "RA" or inData == "RE" or inData == "RB" or inData == "IB" or inData == "IE":
            data = raw_input("Enter data: ")
            command[inData](data)
         elif inData == "IA":
            data = raw_input("Enter data: ")
            dataAfter = raw_input("Enter node data to add after: ") 
            command[inData](data,dataAfter)
         elif inData == "F":
            pos = raw_input("Enter position: ")
            while not pos.isdigit():
               pos = raw_input("Enter position: ")
            output = command[inData](int(pos))
         else:
            output = command[inData]()
            if inData == "C" or inData == "FM":
               print output
      elif inData == "Q":
         run = False
      elif inData == "H":
         print "IB - insert in beginning, IE - insert at end, IA - insert after,"
         print "RB - remove begininng, RE - remove end, RA - remove after,"
         print "F - find node at position, C - count number of nodes, FM - find middle node,"
         print "P - print list, Q - quit"
      else:
         print "Command not found"

#PURPOSE:   Runs demo for stack
#INPUT:     NONE
#OUTPUT:    NONE
def runStack():
   run = True
   myStack = stack.Stack()
   command = { "PUSH" : myStack.push,
               "POP" : myStack.pop,
               "TOP" : myStack.top,
               "E" : myStack.isEmpty,
               "S" : myStack.getSize,
   }

   while run:
      inData = raw_input("Enter Command(H - for Help): ")
      inData = inData.replace(" ", "")
      inData = inData.upper() 

      if inData in command:
         output = ""
         if inData == "PUSH":
            data = raw_input("Enter data: ")
            command[inData](data)
         else:
            output = command[inData]()
            print output 
      elif inData == "Q":
         run = False
      elif inData == "H":
         print "PUSH - To push new data onto stack, POP - To pop data from stack,"
         print "TOP - To get data at top of stack, E - To check if stack empty,"
         print "S - To get size of stack, P - print list, Q - quit"
      else:
         print "Command not found"

#PURPOSE:   Runs demo for queue
#INPUT:     NONE
#OUTPUT:    NONE
def runQueue():
   run = True
   myQueue = None
   command = None

   qType = raw_input("Choice queue type list - L or circular array -CA: ")
   qType = qType.replace(" ", "")
   qType = qType.upper() 
   if qType == "CA":
      qSize = raw_input("Enter circular array size: ")
      while not qSize.isdigit():
         qSize = raw_input("Enter circular array size: ")
      myQueue = queue.Queue(int(qSize))
      command = { "ENQ" : myQueue.enqueue,
                  "DEQ" : myQueue.dequeue,
                  "F" : myQueue.front,
                  "E" : myQueue.isEmpty,
                  "S" : myQueue.getSize,
      }
   else:
      myQueue = queue.Queue()
      command = { "ENQ" : myQueue.arrEnqueue,
                  "DEQ" : myQueue.arrDequeue,
                  "F" : myQueue.arrFront,
                  "FU" : myQueue.arrIsFull,
                  "E" : myQueue.arrIsEmpty,
                  "S" : myQueue.arrGetSize,
      }

   while run:
      inData = raw_input("Enter Command(H - for Help): ")
      inData = inData.replace(" ", "")
      inData = inData.upper() 

      if inData in command:
         output = ""
         if inData == "ENQ":
            data = raw_input("Enter data: ")
            command[inData](data)
         else:
            if qType == "L" and inData == "FU":
               print "is full doesn't work with list queue"
            else:
               output = command[inData]()
      elif inData == "Q":
         run = False
      elif inData == "H":
         print "ENQ - To enqueue data, DEQ - To dequeue data,"
         print "F - Gets the data at the front queue, FU - Gets the if queue is full(only for array based queue,"
         print "E - Gets the if queue is empty, S - Get queue size, Q - quit"
      else:
         print "Command not found"

#PURPOSE:   Runs demo for bstree
#INPUT:     NONE
#OUTPUT:    NONE
def runBSTree():
   run = True
   myBSTree = bSTree.BSTree()
   myMethod = "N"
   command = { "I" : myBSTree.insertNode,
               "R" : myBSTree.removeNode,
               "F" : myBSTree.findSmallestNodeData,
               "PIO" : myBSTree.printInOrder,
               "PRO" : myBSTree.printPreOrder,
               "PPO" : myBSTree.printPostOrder,
               "PAL" : myBSTree.printAllLevel,
               "POL" : myBSTree.printOneLevel,
               "HE" : myBSTree.getHeight
   }
   rCommand = { "I" : myBSTree.recInsertNode,
                "R" : myBSTree.recRemoveNode,
                "F" : myBSTree.recFindSmallestNodeData,
                "PIO" : myBSTree.recPrintInOrder,
                "PRO" : myBSTree.recPrintPreOrder,
                "PPO" : myBSTree.recPrintPostOrder,
                "PAL" : myBSTree.recPrintAllLevel,
                "POL" : myBSTree.recPrintOneLevel,
                "HE" : myBSTree.recGetHeight
   }
   
   while run:
      output = None
      inData = raw_input("Enter Command(H - for Help): ")
      inData = inData.replace(" ", "")
      inData = inData.upper() 

      if inData in command:
         myMethod = raw_input("Enter method to use R - for recusive, N - for iterative: ")
         myMethod = myMethod.replace(" ", "")
         myMethod = myMethod.upper() 
         if myMethod == "R":
            if inData == "I" or inData == "R":
               data = raw_input("Enter data: ")
               myBSTree.root = rCommand[inData](data, myBSTree.root)
            elif inData == "POL":
               lvl = raw_input("Enter level: ")
               while not lvl.isdigit():
                  lvl = raw_input("Enter level: ")
               output = rCommand[inData](myBSTree.root, lvl)
            else:
               output = rCommand[inData](myBSTree.root)
            if output != None:
               print output
         elif myMethod == "N":
            if inData == "I" or inData == "R":
               data = raw_input("Enter data: ")
               command[inData](data)
            elif inData == "POL":
               lvl = raw_input("Enter level: ")
               while lvl.isdigit():
                  lvl = raw_input("Enter level: ")
               output = command[inData](lvl)
            else:
               output = command[inData]()
            if output != None:
               print output
         else:
            print "Method not recognized"
      elif inData == "Q":
         run = False
      elif inData == "H":
         print "I - Insert data(data must be number values or can have unknown results),"
         print "R - Remove data from tree, F - Find smallest data, PIO - Print tree in order,"
         print "PRO - Print tree in pre order, PPO - Print tree in post order,"
         print "PAL - Print tree in level order, POL - Print one level of tree,"
         print "HE - Get tree height"
      else:
         print "Command not found"

#PURPOSE:   Runs demo for avltree
#INPUT:     NONE
#OUTPUT:    NONE
def runAVLTree():
   run = True
   myAVLTree = aVLTree.AVLTree()
   myMethod = "N"
   command = { "I" : myAVLTree.insertNode,
               "R" : myAVLTree.removeNode,
               "F" : myAVLTree.findSmallestNodeData,
               "PIO" : myAVLTree.printInOrder,
               "PRO" : myAVLTree.printPreOrder,
               "PPO" : myAVLTree.printPostOrder,
               "PAL" : myAVLTree.printAllLevel,
               "POL" : myAVLTree.printOneLevel,
               "HE" : myAVLTree.getHeight
   }
   rCommand = { "I" : myAVLTree.recInsertNode,
                "R" : myAVLTree.recRemoveNode,
                "F" : myAVLTree.recFindSmallestNodeData,
                "PIO" : myAVLTree.recPrintInOrder,
                "PRO" : myAVLTree.recPrintPreOrder,
                "PPO" : myAVLTree.recPrintPostOrder,
                "PAL" : myAVLTree.recPrintAllLevel,
                "POL" : myAVLTree.recPrintOneLevel,
                "HE" : myAVLTree.recGetHeight
   }
   
   while run:
      output = None
      inData = raw_input("Enter Command(H - for Help): ")
      inData = inData.replace(" ", "")
      inData = inData.upper() 

      if inData in command:
         myMethod = raw_input("Enter method to use R - for recusive, N - for iterative: ")
         myMethod = myMethod.replace(" ", "")
         myMethod = myMethod.upper() 
         if myMethod == "R":
            if inData == "I" or inData == "R":
               data = raw_input("Enter data: ")
               myAVLTree.root = rCommand[inData](data, myAVLTree.root)
            elif inData == "POL":
               lvl = raw_input("Enter level: ")
               while not lvl.isdigit():
                  lvl = raw_input("Enter level: ")
               output = rCommand[inData](myAVLTree.root, lvl)
            else:
               output = rCommand[inData](myAVLTree.root)
            if output != None:
               print output
         elif myMethod == "N":
            if inData == "I" or inData == "R":
               data = raw_input("Enter data: ")
               command[inData](data)
            elif inData == "POL":
               lvl = raw_input("Enter level: ")
               while lvl.isdigit():
                  lvl = raw_input("Enter level: ")
               output = command[inData](lvl)
            else:
               output = command[inData]()
            if output != None:
               print output
         else:
            print "Method not recognized"
      elif inData == "Q":
         run = False
      elif inData == "H":
         print "I - Insert data(data must be number values or can have unknown results),"
         print "R - Remove data from tree, F - Find smallest data, PIO - Print tree in order,"
         print "PRO - Print tree in pre order, PPO - Print tree in post order,"
         print "PAL - Print tree in level order, POL - Print one level of tree,"
         print "HE - Get tree height"
      else:
         print "Command not found"

if __name__ == '__main__':
   if len(sys.argv) >= 2:
      if sys.argv[1] == "1" or sys.argv[1] == "Stack":
         print "Stack"
         runStack()
      elif sys.argv[1] == "2" or sys.argv[1] == "Queue":
         print "Queue"
         runQueue()
      elif sys.argv[1] == "3" or sys.argv[1] == "BSTree":
         print "BSTree"
         runBSTree()
      elif sys.argv[1] == "4" or sys.argv[1] == "AVLTree":
         print "AVLTree"
         runAVLTree()
      else:
         print "LinkList"
         runLinkList()
   else:
      print "LinkList"
      runLinkList()


