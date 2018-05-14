1. Build heap:

```
def GenerateSwaps(self):
  # The following naive implementation just sorts
  # the given sequence using selection sort algorithm
  # and saves the resulting sequence of swaps.
  # This turns the given array into a heap,
  # but in the worst case gives a quadratic number of swaps.
  #
  # TODO: replace by a more efficient implementation
  size = len(self._data)
  for i in range(((size) // 2), -1, -1):
      self.SiftDown(i) # 从叶到根来排列，这样每到一层，其枝叶都已经排列好了


def SiftDown(self, i):
    minIndex, size = i, len(self._data)
    while minIndex < size:
        # l_index = 2i + 1, r_index = 2i + 2
        l, r, temp = 2*minIndex + 1, 2*minIndex + 2, minIndex
        if l < size and self._data[l] < self._data[temp]:
            temp = l
        if r < size and self._data[r] < self._data[temp]:
            temp = r
        if temp != minIndex: #如果上面一波比较后发现children中有更小的，那么就把小的换上来，并记录交换
            self._data[temp], self._data[minIndex] =  self._data[minIndex], self._data[temp]
            self._swaps.append((minIndex, temp))
            minIndex = temp # 将minIndex换到下面子项
        else:
            break #如果children都比自己小的话就不用继续下移了，终止循环

```

2. job JobQueue

这道题的思路是，将workers依照 开始空闲的时刻 做一个minHeap，root是空闲时刻最小的
一开始空闲时刻均为0. 当一个worker接下一个任务时，其空闲时刻要加上这个任务所需用时。
所以loop任务集，对于每一项任务，在worker中找到空闲时刻最小，也就是最快能接受这个任务的
worker，来干这个任务，记录下它的编号和接手时刻。这个worker也就是root。然后更新root的空闲时间，
siftDown root以换上此时空闲时刻最小的worker。 循环往复直到最后一个任务


```
def SiftDown(self, i):
  minIndex, size = i, self.num_workers
  while minIndex < size:
      # l_index = 2i + 1, r_index = 2i + 2
      l, r, temp = 2*minIndex + 1, 2*minIndex + 2, minIndex
      # 选择时刻小，或者时刻相同但是id小的
      if l < size:
          A = self.next_free_time[l]["freeTime"] < self.next_free_time[temp]["freeTime"]
          B = self.next_free_time[l]["freeTime"] == self.next_free_time[temp]["freeTime"] and self.next_free_time[l]["id"] < self.next_free_time[temp]["id"]
          if (A or B):
              temp = l
      if r < size:
          A = self.next_free_time[r]["freeTime"] < self.next_free_time[temp]["freeTime"]
          B = self.next_free_time[r]["freeTime"] == self.next_free_time[temp]["freeTime"] and self.next_free_time[r]["id"] < self.next_free_time[temp]["id"]
          if (A or B):
              temp = r
      if temp != minIndex: #如果上面一波比较后发现children中有更小的，那么就把小的换上来，并记录交换
          self.next_free_time[temp], self.next_free_time[minIndex] =  self.next_free_time[minIndex].copy(), self.next_free_time[temp].copy()
          minIndex = temp
      else:
          break #如果children都比自己小的话就不用继续下移了，终止循环

def SiftUp(self, i):
    while i > 0:
        parent = (i - 1) // 2
        A = self.next_free_time[parent]["freeTime"] > self.next_free_time[i]["freeTime"]
        B = self.next_free_time[parent]["freeTime"] == self.next_free_time[i]["freeTime"] and self.next_free_time[parent]["id"] > self.next_free_time[i]["id"]
        if A or B:
            self.next_free_time[parent], self.next_free_time[i] = self.next_free_time[i].copy(), self.next_free_time[parent].copy()
            i = parent
        else:
            break
def ExtractMin(self, time):# 获取root+changePriority(root)
    res = self.next_free_time[0].copy() # 只有这样copy的字典才不会随原字典变化
    self.next_free_time[0]["freeTime"] += time
    self.SiftDown(0) # 更新root，然后向下检查寻找比它大的
    return res

def assign_jobs(self):
    # TODO: replace this code with a faster algorithm.
    self.assigned_workers = [None] * len(self.jobs)
    self.start_times = [None] * len(self.jobs)
    self.next_free_time = [{"id": i, "freeTime": 0} for i in range(self.num_workers)]
    for i in range(len(self.jobs)): #循环每一项任务，从工人中找出最快能闲下来的人来干活，并且更新这个工人下一次闲下来时间
      next_worker = self.ExtractMin(self.jobs[i])
      self.assigned_workers[i] = next_worker["id"]
      self.start_times[i] = next_worker["freeTime"]
```

3. merge table

getParent(): use while loop or recursion both ok
merge(): use rank heuristic just like in the lecture,
merge the tree with lower height into the tree with higher height.
Example:

table 1 2 3 4 5

rows 1 1 1 1 1

merge 5 into 3: 3 has 2 rows

merge 2 into 4: 2 has 2 rows

merge 1 into 4: 2 has 3 rows. Actually 1 has 3 rows but
because 1's height = 1 and 2's height = 2 so we merge 1 into 2 and so 2 has 3 rows.
Later when we want to do something with 1, getParent(1) will returns 2 and lines[2] is 3.
So you still can say that the number of rows of table 1 is 3.
如果在merge时候不考虑rank，那么就会在#116出错过不去
所以即使是使用了path compression，merge时候也必须用rank

```
# python3
import sys
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table): # 使用path compression的方法
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return lines[realDestination]

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size
    if rank[realDestination] >= rank[realSource]:   # 这里一定要是把短的tree接到长的tree上，否则会fail #116
        lines[realDestination] += lines[realSource]
        parent[realSource] = realDestination
        lines[realSource] = 0
        if rank[realSource] == rank[realDestination]:   # 两个tree相同时候rank += 1
            rank[realDestination] += 1
        return lines[realDestination]

    else:
        lines[realSource] += lines[realDestination]
        parent[realDestination] = realSource
        lines[realDestination] = 0
        return lines[realSource]

for i in range(m): #避免timelimit exceed：DON'T call max() function again, whether in merge() or in for loop,
    destination, source = map(int, sys.stdin.readline().split())#  Just compare the merge root to previous ans
    val = merge(destination - 1, source - 1)
    if ans < val:
        ans = val
    print(ans)
# python merging_tables.py

```
