# python3
'''
这道题的思路是，将workers依照 开始空闲的时刻 做一个minHeap，root是空闲时刻最小的
一开始空闲时刻均为0. 当一个worker接下一个任务时，其空闲时刻要加上这个任务所需用时。
所以loop任务集，对于每一项任务，在worker中找到空闲时刻最小，也就是最快能接受这个任务的
worker，来干这个任务，记录下它的编号和接手时刻。这个worker也就是root。然后更新root的空闲时间，
siftDown root以换上此时空闲时刻最小的worker。 循环往复直到最后一个任务
'''
class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

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
        self.SiftDown(0) # 更新root，然后想下检查寻找比它大的
        return res

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.next_free_time = [{"id": i, "freeTime": 0} for i in range(self.num_workers)]
        for i in range(len(self.jobs)):
          next_worker = self.ExtractMin(self.jobs[i])
          self.assigned_workers[i] = next_worker["id"]
          self.start_times[i] = next_worker["freeTime"]

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
