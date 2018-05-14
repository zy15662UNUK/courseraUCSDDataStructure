# python3

import sys

class Rope:
	def __init__(self, s):
		self.s = s
	def result(self):
		return self.s
	def process(self, i, j, k):
		cut_out = self.s[i:j+1]
		remain = self.s[0:i] + self.s[j+1:]
		self.s = remain[0:k] + cut_out + remain[k:]

rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
	i, j, k = map(int, sys.stdin.readline().strip().split())
	rope.process(i, j, k)
print(rope.result())
