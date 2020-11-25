from collections import deque


queue = deque()
n = int(input())
for _i in range(n):
    comm = input().split()
    if comm[0] == "ISSUE":
        queue.appendleft(int(comm[1]))
    elif comm[0] == "SOLVED":
        queue.pop()
for _i in range(len(queue)):
    print(queue.pop())
