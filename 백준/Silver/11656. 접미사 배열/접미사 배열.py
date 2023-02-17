S = input()
result = [S[i:] for i in range(len(S))]

for i in sorted(result):
    print(i)