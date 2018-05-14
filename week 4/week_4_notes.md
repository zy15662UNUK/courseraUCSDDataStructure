1. Hash functions:
实际上它建立了keys到储存数据的array的index一个映射。
因为一旦index < keys，也就是储存用的array内空格数目小于总的objects数目。
每个格子里就可能有多个key，或者说object。这些key用hash function算出来index会是相同的
这时候就要将这些共用的key串在一个list里。到时候算出一个index后，就将对应list中项目一个个排查
直到找出需要的。所以说最棒的情况是一个index里面一个key，但这样要求很多存储空间。如果index少的话
每个里面的list又会太长。所以我们希望index数目适中，keys均匀分布在index上

n是被储存的object数目，m是index数目
Pr[h(x) = h(y)] ≤ 1/m, 我们希望重叠率<=1/m
load factor 𝛼=n/m 0.5 < 𝛼 < 1

2. Hashing integers
h (x) = ((ax + b) mod p) mod m
x is the integer key value
p is prime number bigger than n
1 ≤ a ≤ p − 1, 0 ≤ b ≤ p − 1

3. Hashing strings
PolyHash(S, p, x)
  hash ← 0
  for i from |S| − 1 down to 0:
    hash ← (hash × x + S[i ]) mod p
  return hash

with a fixed prime p and all 1 ≤ x ≤ p − 1 is
called polynomial

Example: |S| = 3
1 hash = 0
2 hash = S[2] mod p
3 hash = S[1] + S[2]x mod p
4 hash = S[0] + S[1]x + S[2]x2 mod p

4. Searching patterns:
如果要寻找一个长字符串中某个短字符串出现的次数和位置，naive方法是遍历长串中每个长度为短字符串
pattern的子字符串，然后进行比较，如果和pattern相同，那么结果的list中+1
这样实在是太笨了，花的时间至少为n*p，n是长字符串的长度，p是pattern的长度

使用Rabin-Karp's Algorithm
先把长字节中所有长度为pattern的子字符串储存在一个hash table中
使用hash function给pattern算出一个index值，然后搜寻hash table中这个index的值，从中找出和pattern相同的

在使用hash function的时候，实际上相邻两项子字符算出的index值的差别非常小，且是固定的，因此只需要算出最后一个
子字节的index值，而后前面每一个子字节的index值都是由后一个子字符串修改得出的：
H[i ] = x*H[i + 1] + (T[i ] − T[i + |P|]*x^|P|) mod p

PrecomputeHashes(T, |P|, p, x)
  H ← array of length |T| − |P| + 1 #有|T| − |P| + 1个子字符串
  S ← T[|T| − |P|..|T| − 1] #S是最后一个子字符串
  H[|T| − |P|] ← PolyHash(S, p, x)  #计算最后一个子字符串的hash table index
  y ← 1
  for i from 1 to |P|:  #计算x^|P|的值
    y ← (y × x) mod p
  for i from |T| − |P| − 1 down to 0: #从后往前迭代修改出每一个子字节的index值
    H[i ] ← (xH[i + 1] + T[i ] − yT[i + |P|]) mod p
  return H  #H最后是一个长度为子字符串数目的array，每一项内容为每个子字符串的hash index值


 RabinKarp(T, P)
  p ← big prime, x ← random(1, p − 1)
  result ← empty list
  pHash ← PolyHash(P, p, x) #算出pattern的hash table index
  H ← PrecomputeHashes(T, |P|, p, x)  #利用上面的fun搭建hash table
  for i from 0 to |T| − |P|:  遍历这个hash table
    if pHash != H[i ]:
      continue
    if AreEqual(T[i ..i + |P| − 1], P): #当hash index的值和pattern的hash index值相等时候，对比两个字符串是否全等
      result.Append(i)
  return result
