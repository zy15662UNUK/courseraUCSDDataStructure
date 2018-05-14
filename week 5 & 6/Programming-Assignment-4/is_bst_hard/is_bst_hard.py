#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

result = []
result_index = []
def inOrder(tree):
  inorer_tranverse(0, tree)
  return result

def inorer_tranverse(nodeIndex, tree):
    if tree[nodeIndex][1] != -1:
        inorer_tranverse(tree[nodeIndex][1], tree)
    result.append(tree[nodeIndex][0])
    result_index.append(nodeIndex)  #需要一个平行的list来记录每一个key对应的index，因为有这个index就可以方便在tree里找它的左右child
    if tree[nodeIndex][2] != -1:
        inorer_tranverse(tree[nodeIndex][2], tree)

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) > 1:
      inOrder(tree)
      for i in range(len(result) - 1):
          if result[i] > result[i+1]:
              return False
          if result[i] == result[i+1]: #因为左侧必须严格小于parent，因此相邻相等情况下，如果是leftChild+parent相等的话
              if result_index[i] == tree[result_index[i+1]][1]:#所以就检查i项是不是i+1项leftchild，是的话就False
                  return False
  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
