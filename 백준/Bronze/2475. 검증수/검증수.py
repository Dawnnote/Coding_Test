num = list(map(int, input().split()))
result = [i**2 for i in num]
print(sum(result)%10)