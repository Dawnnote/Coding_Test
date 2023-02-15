A = int(input())
B = int(input())
C = int(input())

abc_sum = A*B*C
abc_str = str(abc_sum)
for i in range(0, 10):
    print(abc_str.count(str(i)))