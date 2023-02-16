def dfs(n):
  if len(num) == len(L):
    print("".join(num))
    return

  for i in range(len(L)):
    if check[i] == False:
      check[i] = True
      num.append(L[i])
      dfs(i)
      check[i] = False
      num.pop()
      
T = int(input())
for i in range(1, T+1):
  L = input()
  num = []
  check = [False]*len(L)

  print(f'Case # {i}:')
  dfs(0)