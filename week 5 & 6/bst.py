class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:   #如果是第一个node
            self.root = Node(data)
        else:
            node = Node(data)
            self.insertNode(node, self.root)

    def insertNode(self, node, root):
        if node.data < root.data:
            if not root.leftChild:
                root.leftChild = node
            else:   #如果leftchild存在，则继续往下找
                self.insertNode(node, root.leftChild)
        else:
            if not root.rightChild:
                root.rightChild = node
            else:
                self.insertNode(node, root.rightChild)
    def getMinVal(self):
        if self.root:
            return self.getMin(self.root)
        else:
            print("Empty tree")
    def getMin(self, node):
        if node.leftChild:  #如果有比这个node小的
            return self.getMin(node.leftChild)  #那么继续试图寻找比leftchild更小的
        return node.data    #否则返回这个node
    def getMaxVal(self):
        if self.root:
            return self.getMax(self.root)
        else:
            print("Empty tree")
    def getMax(self, node):
        if node.rightChild:  #如果有比这个node大的
            return self.getMax(node.rightChild)  #那么继续试图寻找比leftchild更大的
        return node.data    #否则返回这个node

    def tranverseTree(self):
        if self.root:
            return self.tranverse(self.root)
        else:
            print("Empty tree")
    def tranverse(self, node):
        # 按照左中右的顺序print
        if node.leftChild:  #在左边有child情况下，把最左边一路捅穿
            self.tranverse(node.leftChild)
        print(node.data)    #print当前node
        if node.rightChild: #捅穿右边
            self.tranverse(node.rightChild)
        # 执行顺序是：最开始一路捅到最左边，print，返回执行上一个函数的print，也就是最后一个node中间
        # 然后捅右边，print，回去执行上一个没执行完的
    def remove(self, data):
        if self.root:
            self.root = self.removeItem(data, self.root)
        else:
            print("Empty tree")
    def removeItem(self, data, node):
        if not node:    #如果这个node不存在，直接返回
            return node
        if data < node.data:    #如果这个要被删的data<node，往左迭代更新 node leftChild
            node.leftChild = self.removeItem(data, node.leftChild)#如果没有leftchild，那么返回给leftchild none
        elif data > node.data:  #如果这个要被删的data>node，往右迭代更新node rightChild
            node.rightChild = self.removeItem(data, node.rightChild)
        else: #如果这个node就是要找的,分3种情况处理
            if not node.leftChild and not node.rightChild:  #如果这个node没有children
                del node    #删除node
                return None #返回一个none给上一个叫它的parent.e.x.: node.leftChild = None, node 为parent
            if not node.leftChild:  #如果只有rightchild
                temp = node.rightChild  #提出rightchild
                del node    #删除node
                return temp #把rightchild代替他作为叫它的parent的child
            elif not node.rightChild:
                temp = node.leftChild
                del node
                return temp
            # 如果说这个node有两个children，那么我们先找左边children中最大的作为它的继任者，然后删掉原来左边最大的
            temp = self.getPredeccsor(node.leftChild)   #找到继任者
            node.data = temp.data   #继任者上位
            node.leftChild = self.removeItem(temp.data, node.leftChild) #干掉原来位置上继任者，这时候只可能是没有child或者一个child
        return node #返回新继任者

    def getPredeccsor(self, node):
        if node.rightChild:
            return self.getPredeccsor(node.rightChild)
        return node

list, tree = [2,3,1,44,111,2,3,222,4,10,1], BST()
for i in list:
    tree.insert(i)
tree.tranverseTree()
tree.remove(0)
tree.tranverseTree()
print("max: ", tree.getMaxVal())
print("min: ", tree.getMinVal())
