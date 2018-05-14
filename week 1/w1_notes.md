- BFS 遍历tree并统计树高:

```
def compute_height(self):
      # 使用bfs方法，每搜索完一层则层数加一，当把每一层搜完之后得出高度即是tree的高度
      q, root, tree, height = [], None, [{"id": i, "ch": []} for i in range(len(self.parent))], 1
      for i in range(len(self.parent)):# 建造树，loop每一项，将parent和child建立联系
          if self.parent[i] == -1:
              root = i
          else:
              tree[self.parent[i]]["ch"].append(i)# child都添加到parent的child表中
      if len(tree[root]["ch"]) == 0:# 如果root没有child，那么直接返回1
          return height
      q, count = [tree[root]], len(tree[root]["ch"])+1 # q是装每一层的nodes的queue，
      # count是用来统计每层nodes数的，当每层的node都操作完之后，层数即可加一
      while len(q) > 0: # 当q里面有东西时,意味着还有node没有处理完
          if count == 0:# 检查这一层的node是否处理完
              height += 1# 处理完则加一
              count += len(q)# 此时q中应该只剩下下一层的全部nodes,给count换上下一层的node数
          node = q.pop(0)# 拿出queue中第一项并从queue中删除, 因为queue是"先进先出",这样保证一层的处理完才处理下一层
          for j in node["ch"]:# 将拿出来这一项的children都加入queue中
              q.append(tree[j])
          count -= 1# 处理完一项,count-1
      return height + 1# 因为最后一层当count等于0时queue也等于0了.因此while终止,所以要在最后把这一层加上

```
- DFS 方法遍历tree并统计tree高度

```
PreOrderTraversal(tree)
  if tree = nil: # 如果tree是空的, 直接终止
    return
  Print(tree.key)# 先print当前node, 然后依次搜索左右child,也就是print会是从root开始先往左侧print
  PreOrderTraversal(tree.left)
  PreOrderTraversal(tree.right)


PostOrderTraversal(tree)
  if tree = nil:
    return
  PostOrderTraversal(tree.left)
  PostOrderTraversal(tree.right)
  Print(tree.key)# 先完成搜索左右child再print,也就是print会是从最末端node开始, 末端左,末端右,parent

InOrderTraversal(tree)
  if tree = nil:
    return
  InOrderTraversal(tree.left)
  Print(tree.key)# print顺序: 末端左,parent,末端右
  InOrderTraversal(tree.right)
```
