n = int(input())
a = list(map(int, input().split()))
mx = max(a)
sum = 0

for i in range(n):
    a[i] = a[i]/mx*100
    sum += a[i]

print(sum/n)