S = input()

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = [0]*26

for i in range(len(S)):
    if S[i] in abc:
        num[abc.index(S[i])] += 1

print(" ".join(map(str, num)))