# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

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
              minIndex = temp
          else:
              break #如果children都比自己小的话就不用继续下移了，终止循环

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
