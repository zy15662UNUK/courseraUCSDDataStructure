# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.inorer_tranverse(0)
    return self.result

  def inorer_tranverse(self, nodeIndex):
      if self.left[nodeIndex] != -1:
          self.inorer_tranverse(self.left[nodeIndex])
      self.result.append(self.key[nodeIndex])
      if self.right[nodeIndex] != -1:
          self.inorer_tranverse(self.right[nodeIndex])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.preOrder_tranverse(0)
    return self.result

  def preOrder_tranverse(self, nodeIndex):
      self.result.append(self.key[nodeIndex])
      if self.left[nodeIndex] != -1:
          self.preOrder_tranverse(self.left[nodeIndex])
      if self.right[nodeIndex] != -1:
          self.preOrder_tranverse(self.right[nodeIndex])


  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postOrder_tranverse(0)
    return self.result

  def postOrder_tranverse(self, nodeIndex):
      if self.left[nodeIndex] != -1:
          self.postOrder_tranverse(self.left[nodeIndex])
      if self.right[nodeIndex] != -1:
          self.postOrder_tranverse(self.right[nodeIndex])
      self.result.append(self.key[nodeIndex])

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
