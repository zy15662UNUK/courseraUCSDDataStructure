
class Node(object):

        def __init__(self, data):
                self.data = data;# set the value for each node
                self.leftChild = None;
                self.rightChild = None;# values at the beginning 
                
class BinarySearchTree(object):

        def __init__(self):
                self.root = None;# init is to set the beginning value
                
        def insert(self, data):# like a trigger for seteing nodes
                if not self.root:# if there is no nodes
                        self.root = Node(data);
                else:
                        self.insertNode(data, self.root);
                        
        # O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
        def insertNode(self, data, node):# set the data to be a child of the input
                                         #node
        
                if data < node.data:
                        if node.leftChild:# if the node has a child on the left
                                          # go recursion 
                                self.insertNode(data, node.leftChild);
                        else:# if there is no child
                                node.leftChild = Node(data);
                else:# go to right, same step as 
                        if node.rightChild:
                                self.insertNode(data, node.rightChild);
                        else:
                                node.rightChild = Node(data);
        
        # O(logN)       
        def removeNode(self, data, node):
        
                if not node:
                        return node;
                        
                if data < node.data:
                        node.leftChild = self.removeNode(data, node.leftChild);
                elif data > node.data:
                        node.rightChild = self.removeNode(data, node.rightChild);
                else:
                        
                        if not node.leftChild and not node.rightChild:
                                print("Removing a leaf node...");
                                del node;
                                return None;
                                
                        if not node.leftChild:  # node !!!
                                print("Removing a node with single right child...");
                                tempNode = node.rightChild;
                                del node;
                                return tempNode;
                        elif not node.rightChild:   # node instead of self
                                print("Removing a node with single left child...");
                                tempNode = node.leftChild;
                                del node;
                                return tempNode;
                        
                        print("Removing node with two children....");
                        tempNode = self.getPredecessor(node.leftChild);   # self instead of elf  + get predecessor 
                        node.data = tempNode.data;
                        node.leftChild = self.removeNode(tempNode.data, node.leftChild);
                
                return node;   # !!!!!!!!!!!!

        def getPredecessor(self, node):
        
                if node.rightChild:
                        return self.getPredeccor(node.rightChild);
                        
                return node;
                
        def remove(self, data):
                if self.root:
                        self.root = self.removeNode(data, self.root);
                        
                # O(logN)
        def getMinValue(self):# trigger function for the root
                if self.root:
                        return self.getMin(self.root);
                        
        def getMin(self, node):
        
                if node.leftChild:# if the left child is not a None
                        return self.getMin(node.leftChild);
                        
                return node.data;
                
                # O(logN)
        def getMaxValue(self):
                if self.root:
                        return self.getMax(self.root);
                        
        def getMax(self, node):
        
                if node.rightChild:
                        return self.getMax(node.rightChild);
                        
                return node.data;
                
        def traverse(self):
                if self.root:
                        self.traversePostOrder(self.root);
                        
                        # O(N)
        def traverseInOrder(self, node):# In-order traversal: we visit the left subtree + the root node +
                                        # the right subtree recursively !!!

                if node.leftChild:
                        self.traverseInOrder(node.leftChild);
                        
                print("%s " % node.data);
'''
 This print will be executed only when the ahead 'if'statement is passed. i.e. ppt bst.  find the leftest one(1), print it.
 Go back to last recursion,which is its parent node(10),print it, goes to the right(19), check, goes left(16),print. then right(23)..and so on
'''                 
                
                if node.rightChild:# start when the leftest is found
                        self.traverseInOrder(node.rightChild);
                        
##              print("%s " % node.data);
        def traversePostOrder(self, node):# Post-order traversal: we visit the left subtree+ right subtree +
                                          # the root recursively !!!

                if node.leftChild:
                        self.traversePostOrder(node.leftChild);
                        

                
                if node.rightChild:
                        self.traversePostOrder(node.rightChild);
                        
                print("%s " % node.data);
        def traversePreOrder(self, node):# Pre-order traversal: we visit the root+ left subtree +
                                         #the right subtree recursively !!!
                print("%s " % node.data);
                if node.leftChild:
                        self.traversePreOrder(node.leftChild);           
                if node.rightChild:             
                        self.traversePreOrder(node.rightChild); 
                        
                
                        
                        
                
                        

                
                
                        
                        
                
        

bst = BinarySearchTree();
bst.insert(32);
bst.insert(10);
bst.insert(1);
bst.insert(19);
bst.insert(16);
bst.insert(23);
bst.insert(55);
bst.insert(79);
##bst.remove(10);

bst.traverse();
