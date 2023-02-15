t_case = int(input())

for _ in range(t_case):
    l_case = list(input())
    cnt = 0
    add = 0
    for i in l_case:
        if i == 'O':
            cnt += 1
            add += cnt
        else:
            cnt = 0
    print(add)