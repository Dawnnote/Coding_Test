n = []
for i in range(10):
    a = int(input())
    n.append(a%42)

print(len(set(n)))