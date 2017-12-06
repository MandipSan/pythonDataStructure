PP = python 
PFLAGS = -m

#To run demo for link list
runLinkList: dataStructure/linkList.py 
	@$(PP) $(PFLAGS) demo 

#To run demo for stack
runStack: dataStructure/stack.py
	@$(PP) $(PFLAGS) demo Stack

#To run demo for queue
runQueue: dataStructure/queue.py
	@$(PP) $(PFLAGS) demo Queue

#To run for bstree
runBSTree: dataStructure/bSTree.py
	@$(PP) $(PFLAGS) demo BSTree

#To run for avltree
runAVLTree: dataStructure/aVLTree.py
	@$(PP) $(PFLAGS) demo AVLTree

#To run all test for all data structure
testAll: testLinkList testStack testQueue testBSTree testAVLTree

#To run link list test
testLinkList: dataStructure/linkList.py testModules/linkListTest.py
	@$(PP) $(PFLAGS) testModules.linkListTest

#To run stack test
testStack: dataStructure/stack.py testModules/stackTest.py 
	@$(PP) $(PFLAGS) testModules.stackTest

#To run queue test
testQueue: dataStructure/queue.py testModules/queueTest.py
	@$(PP) $(PFLAGS) testModules.queueTest

#To run BSTree test
testBSTree: dataStructure/bSTree.py testModules/bSTreeTest.py
	@$(PP) $(PFLAGS) testModules.bSTreeTest

#To run AVLTree test
testAVLTree: dataStructure/aVLTree.py testModules/aVLTreeTest.py
	@$(PP) $(PFLAGS) testModules.aVLTreeTest

#To remove all .pyc files
clean:
	@find . -type f -name '*.pyc' -exec rm {} +
