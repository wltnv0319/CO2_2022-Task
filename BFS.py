import sys
from collections import deque

# 14248번 : 점프점프 (실패)
def N_14248():
    n = int(input())
    Array = list(map(int, input().split()))

    start = int(input()) -1
    visited = [0] * n

    result = 0

    def bts(start):
        global result
        queue = deque()
        queue.append(start)
        visited[start] =1 
        result += 1
        
        while queue:
            node= queue.popleft()
            for cnt_i in [-Array[node], Array[node]]:
                temp = node + cnt_i
                if 0 <= temp < n and visited[temp] ==0:
                    queue.append(temp)
                    result += 1
                    visited[temp] = 1

# 14217번 : 그래프 탐색 (실패)
def N_14217():
    n,m = map(int, sys.stdin.readline().split(" "))
    c = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split(" "))
        c[a].append(b)
        c[b].append(a)
        
    def bfs():
        global n
        global c
        visited = [-1 for _ in range(n+1)]
        root = deque([1,0])
        while root:
            pops = root.popleft()
            if visited[pops[0]] == -1:
                visited[pops[0]] = pops[1]
                for cnt_i in c[pops[0]]:
                    if visited[cnt_i] == -1:
                        root.append([cnt_i, pops[1]+[1]])
        return visited

    k = int(sys.stdin.readline())

    for cnt_i in range(k):
        a, count_1, count_2 = map(int, sys.stdin.readline().split(" "))
        if a == 1:
            c[count_1].append(count_2)
            c[count_2].append(count_1)
        else:
            c[count_1].remove(count_2)
            c[count_2].remove(count_1)
        ans = bfs()
        print(0, end=" ")
        
        for cnt_i in range(2, n):
            print(ans[cnt_i], end=" ")
        
        print(ans[n])