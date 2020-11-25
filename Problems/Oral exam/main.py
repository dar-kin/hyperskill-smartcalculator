from collections import deque


q = ""
queue = deque()
n = int(input())
for _i in range(n):
    comm = input().split()
    if comm[0] == "READY":
        queue.appendleft(comm[1])
    elif comm[0] == "PASSED":
        q += queue.pop() + "\n"
    elif comm[0] == "EXTRA":
        queue.appendleft(queue.pop())
print(q[:len(q) - 1])
