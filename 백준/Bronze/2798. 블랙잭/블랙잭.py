import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_num = num[i]+num[j]+num[k]
            if result < sum_num <= M:
                result = sum_num
print(result)