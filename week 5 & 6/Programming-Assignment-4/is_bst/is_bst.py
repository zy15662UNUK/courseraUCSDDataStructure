#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

# 如果这个tree是正确的，那么inorder——tranverse出来的必然是一个严格升序的数组
# 所以通过检查结果数组是不是严格升序就可以判断
result = []
def inOrder(tree):
  inorer_tranverse(0, tree)
  return result

def inorer_tranverse(nodeIndex, tree):
    if tree[nodeIndex][1] != -1:
        inorer_tranverse(tree[nodeIndex][1], tree)
    result.append(tree[nodeIndex][0])
    if tree[nodeIndex][2] != -1:
        inorer_tranverse(tree[nodeIndex][2], tree)

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) > 0:
      inOrder(tree)
      for i in range(len(result) - 1):
          if result[i] >= result[i+1]:
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
