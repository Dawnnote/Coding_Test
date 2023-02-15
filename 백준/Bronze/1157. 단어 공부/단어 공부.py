word = input()
word = word.upper()
s = set(word)

dic = {i:word.count(i) for i in s}

dic_max = max(dic.values())

result = []
for k, v in dic.items():
  if v == dic_max:
    result.append(k)

if len(result) == 1:
  print(result[0])
else:
  print('?')