#10989
# 작성일 : 2021/3/23

import sys

num = int(sys.stdin.readline())
data = [0]*10001

# 입력
for _ in range(num):
    n = int(sys.stdin.readline())
    data[n] += 1
    
for i in range(10001):
    if data[i] != 0:
        for j in range(data[i]):
            sys.stdout.write(str(i) + '\n')