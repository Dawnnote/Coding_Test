import sys
N = int(sys.stdin.readline())

num = []
for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        num.append(int(command[1]))
        
    elif command[0] == 'pop':
        if not num:
            print(-1)
        else:
            print(num.pop())
        
    elif command[0] == 'size':
        print(len(num))
        
    elif command[0] == 'empty':
        if not num:
            print(1)
        else:
            print(0)
            
    elif command[0] == 'top':
        if not num:
            print(-1)
        else:
            print(num[-1])