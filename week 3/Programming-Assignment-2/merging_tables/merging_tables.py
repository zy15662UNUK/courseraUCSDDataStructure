# python3
'''
This is how I passed:

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
'''

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
