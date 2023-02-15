A = list(map(int, input().split()))

if A == sorted(A):
    print('ascending')
elif A == sorted(A, reverse=True):
    print('descending')
else:
    print('mixed')