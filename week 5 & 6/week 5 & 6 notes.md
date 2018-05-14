1. Can the Insert operation be implemented given only Split and Merge operations?

  Yes. First create a new tree with single key - the key to be inserted.
  Then split the current tree by this key. Then merge the left splitted part with the new tree.
  Then merge the result with the right splitted part.

2. Can the Delete operation be implemented given only Split and Merge operations?
  Yes. Suppose we are deleting key xx. Split by the key twice: one split such that all the keys < x<x go to the left left and all the keys x≥x go to the right. Then split the right part of the first split such that all the keys x≤x go to the left and all the keys > x>x go to the right. Then merge the left part of the first split and the right part of the second split - thus leaving out the node with key xx if there was such a node.
3. Splay tree visualization: https://www.cs.usfca.edu/~galles/visualization/SplayTree.html

4. What is going to happen if you forget to splay the last accessed vertex in the implementation of FindFind in case the key was not found in the splay tree?

The tree will work too slow on some sequences of operations.
Correct! See this visualization and try to insert many elements in perfect order starting from an empty tree: insert 11, then 22, then 33, and so on. See how the tree grows unbalanced, it is just a chain! However, by now each operation took O(1)O(1) time, so it's ok. Now think what will happen if you look for element 00 in this tree. If you use the visualization, you will see that you will have to go all the way down through the tree and then find out in the end that you didn't find anything. The tree in the visualization then splays the lowest vertex, and the tree becomes more balanced. But let's suppose you forgot to implement that - then the tree won't change after the call to FindFind. If you then try to find 00 again in the tree, you will have to go all the way down again! So, after inserting nn elements in the tree in the perfect order, if you look for an element that is smaller than all the keys in the tree nn times, then each of the last nn operations will take O(n)O(n) time, so the tree no longer works in amortized O(\log n)O(logn) time!

5. What will happen if you splay the node with the smallest key in a splay tree?

The root of the new tree won't have left child.
Correct! The node with the smallest key will become the root after splaying, and it cannot have a left child, because the key of the left child must be smaller than the key of its parent.

6. What will happen if you select a node NN, splay its predecessor PP (the node with the largest key smaller than the key of NN), then splay the node NN itself?

N will be the root, PP will be the left child of the root, PP won't have a right child.

Correct! After the first splay, PP will become the root. After the second splay, NN will become the root, and PP will become its child, and it will be on the left, because its key is smaller. PP won't have a right child, because a right child of PP must have key bigger than the key of PP, and also it must have key smaller than the key of NN (because it is now in the left subtree of NN), but it can't happen, because PP is the predecessor of NN, so there are no keys between the key of PP and the key of NN.
