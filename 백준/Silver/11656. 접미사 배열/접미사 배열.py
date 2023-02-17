S = input()
result = []

for i in range(len(S)):
    result.append(S[i:])

for j in sorted(result):
    print(j)