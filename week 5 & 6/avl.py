class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 0
class AVL(object):
    def __init__(self):
        self.root = None
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

    def calculateHeight(self, node):
        if not node:
            return -1
        return node.height

    def calculateBalance(self, node):   #返回左侧高度-右侧高度结果
        if not node:    #如果这个node是none，返回0
            return 0
        return self.calculateHeight(node.leftChild) - self.calculateHeight(node.rightChild)
        # 如果返回>1,说明左侧过重需要rotateRight, 如果返回<-1那么右侧过重需要rotateleft

    def rotateRight(self, node):
        temp = node.leftChild   #rotate上去的新root
        t = temp.rightChild     #temp.rightChild变成原root的leftChild
        temp.rightChild = node
        node.leftChild = t
        # 更新rotate后两项的高度
        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        temp.height = max(self.calculateHeight(temp.leftChild), self.calculateHeight(temp.rightChild)) + 1
        return temp  # 返回新的root

    def rotateLeft(self, node):
        temp = node.rightChild
        t = temp.leftChild
        temp.leftChild = node
        node.rightChild = t
        # 更新rotate后两项的高度
        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        temp.height = max(self.calculateHeight(temp.leftChild), self.calculateHeight(temp.rightChild)) + 1
        return temp  # 返回新的root

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):   #data是insert值，node是插入位置
        if not node:    #如果插入位置是空，那么在此处插入并返回Node(data)
            return Node(data)
        if data < node.data:    #如果插入位置不为空且插入值小于此处node值，那么继续尝试插入leftchild位置
            node.leftChild = self.insertNode(data, node.leftChild)
        else:    #如果插入位置不为空且插入值大于此处node值，那么继续尝试插入rightchild位置
            node.rightChild = self.insertNode(data, node.rightChild)
        # 不管上面插了左边还是右边，都要更新这个node的高度
        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        # 此时可能会不平衡，因此需要再执行handleViolation去先平衡tree， 然后再由这个函数返回node值
        return self.handleViolation(data, node)

    def handleViolation(self, data, node):
        balance = self.calculateBalance(node)   #先检查此node是否平衡
        if balance > 1 and data < node.leftChild.data:  #情况1，node左侧重，且data是继续往leftChild左侧加。左侧一条线情况
            return self.rotateRight(node)   #向右rotate并返回新node
        if balance < -1 and data > node.rightChild.data:    #情况2，node右侧重，且data是继续往rightChild右侧加。右侧一条线情况
            return self.rotateLeft(node)
        if balance > 1 and data > node.leftChild.data:    #情况3，node左侧重，且data是往leftChild右侧加。左-右情况
            node.leftChild = self.rotateLeft(node.leftChild)    #先将leftChild及以下左翻
            return self.rotateRight(node)   #向右rotate并返回新node
        if balance < -1 and data < node.rightChild.data:    #情况4，node右侧重，且data是往rightChild左侧加。右-左情况
            node.rightChild = self.rotateRight(node.rightChild)    #先将rightChild及以下右翻
            return self.rotateLeft(node)   #向左rotate并返回新node
        return node #如果本身就是balance，直接返回node
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

        if not node:    #如果tree只有一个node，直接返回
            return node
        # 更新高度
        node.height = max(self.calculateHeight(node.leftChild), self.calculateHeight(node.rightChild)) + 1
        balance = self.calculateBalance(node)   #先检查此node是否平衡
        if balance > 1 and self.calculateBalance(node.leftChild) >= 0:  #情况1，node左侧重，且data是继续往leftChild左侧加。左侧一条线情况
            return self.rotateRight(node)   #向右rotate并返回新node
        if balance < -1 and self.calculateBalance(node.rightChild) <= 0:    #情况2，node右侧重，且data是继续往rightChild右侧加。右侧一条线情况
            return self.rotateLeft(node)
        if balance > 1 and self.calculateBalance(node.leftChild) < 0:    #情况3，node左侧重，且data是往leftChild右侧加。左-右情况
            node.leftChild = self.rotateLeft(node.leftChild)    #先将leftChild及以下左翻
            return self.rotateRight(node)   #向右rotate并返回新node
        if balance < -1 and self.calculateBalance(node.rightChild) > 0:    #情况4，node右侧重，且data是往rightChild左侧加。右-左情况
            node.rightChild = self.rotateRight(node.rightChild)    #先将rightChild及以下右翻
            return self.rotateLeft(node)   #向左rotate并返回新node
        return node #如果本身就是balance，直接返回node

    def getPredeccsor(self, node):
        if node.rightChild:
            return self.getPredeccsor(node.rightChild)
        return node

list, tree = [2,1,1,2,1,3], AVL()
for i in list:
    tree.insert(i)
tree.tranverseTree()
print("root: ", tree.root.data, "balance: ", tree.calculateBalance(tree.root))
tree.remove(2)
tree.remove(2)
tree.tranverseTree()
print("root: ", tree.root.data, "balance: ", tree.calculateBalance(tree.root))
