from collections import deque
import sys
n = int(sys.stdin.readline())
cnt = 0
queue=deque([])
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0]=='push_front':
        queue.appendleft(command[1])
    elif command[0]=='push_back':
        queue.append(command[1])
    elif command[0]=='pop_front':
        if len(queue) > cnt:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0]=='pop_back':
        if len(queue) > cnt:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue) - cnt )
    elif command[0] == 'empty':
        if len(queue)== cnt:
            print(1)
            cnt = 0
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) <= cnt:
               print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) <= cnt:
            print(-1)
        else:
            print(queue[-1])