def dfs(n):
  if n == len(kriii):
    max_num = max(num)
    if max_num == len(num):
      print(*num)
      exit(0)
    return

  if int(kriii[n]) <= 50 and check[int(kriii[n])] == False:
    check[int(kriii[n])] = True
    num.append(int(kriii[n]))
    dfs(n+1)
    check[int(kriii[n])] = False
    num.pop()

  if n < len(kriii)-1 and int(kriii[n:n+2]) <= 50 and check[int(kriii[n:n+2])] == False:
    check[int(kriii[n:n+2])] = True
    num.append(int(kriii[n:n+2]))
    dfs(n+2)
    check[int(kriii[n:n+2])] = False
    num.pop()

kriii = input().strip()
check = [False] * 51
num = []
dfs(0)