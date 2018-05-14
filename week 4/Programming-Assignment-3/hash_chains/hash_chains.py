# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [[] for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(" ".join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if query.ind >= self.bucket_count: #如果超出list范围，也是空出一排
                self.write_chain([])
            else:
                self.write_chain(reversed(self.elems[query.ind])) # 给每个chain加item时候也是加在最后，但是check时候就直接
             # 把list反过来就可以

        elif query.type == 'find':
            key, boolen = self._hash_func(query.s), False
            for s in self.elems[key]:   #key中每一项逐个检查
                if s == query.s:
                    boolen = True
                    break
            self.write_search_result(boolen)
        elif query.type == 'add':
            key = self._hash_func(query.s)
            if query.s not in self.elems[key]:
                self.elems[key].append(query.s)
        else:
            key = self._hash_func(query.s)
            if query.s in self.elems[key]:
                self.elems[key].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
# python hash_chains.py

'''
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good
------------------------------------------------------------------------------
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test
----------------------
3
12
check 0
find help
add help
add del
add add
find add
find del
del del
find del
check 0
check 1
check 2
'''
