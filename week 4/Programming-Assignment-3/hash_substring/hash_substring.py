# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s):  #计算hash index
    ans = 0
    for c in reversed(s): # 字符串的计算法，记得是reversed(s)逆序loop
        ans = (ans * 263 + ord(c)) % 1000000007
    return ans

def precomputeHashes(pattern, text):    #后面均为伪代码python实现
    x, prime = 263, 1000000007
    t, p, y = len(text), len(pattern), 1
    H = [0 for i in range(t - p + 1)]
    S = _hash_func(text[t-p:t])
    H[t-p] = S
    for i in range(p):
        y = (y * x) % prime
    for i in range(t-p-1, -1, -1):
        H[i] = (H[i+1]*x + ord(text[i]) - y*ord(text[i+p])) % prime
    return H

def get_occurrences(pattern, text):
    t, p = len(text), len(pattern)
    pHash = _hash_func(pattern)
    table, result = precomputeHashes(pattern, text), []
    for i in range(len(table)):
        if pHash == table[i]:
            if pattern == text[i:i+p]:
                result.append(i)
    return result
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

# python hash_substring.py
