from collections import deque
import sys
n = int(sys.stdin.readline())
cnt = 0
queue=deque([x for x in range(1,n+1)])

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])