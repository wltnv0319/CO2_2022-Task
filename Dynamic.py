# 5972 사용
import heapq
import sys

# 15989번 : 1,2,3 더하기 4
def N_15989():
    number = int(input())

    list = [1]*10001

    for i in range(2, 10001):
        list[i] += list[i-2]
        
    for i in range(3, 10001):
        list[i] += list[i-3]
        
    for j in range(number):
        temp = int(input())
        print(list[temp])

# 1010번 : 다리 놓기
def N_1010():
    def Factorial(N):
        number = 1
        for i in range(1, N+1):
            number *= i
        return number

    T = int(input())

    for i in range(T):
        n,m = map(int, input().split())
        bridge= Factorial(m) //(Factorial(n)*Factorial(m-n))
        print(bridge)
    
# 다이엑스트라 5972번 : 택배 배송 (실패)
def N_5972():
    input = sys.stdin.readline
    INF = int(1e9)

    N,M = map(int, input().split())

    graph =[[] for i in range(N+1)]
    distance =[INF]*(N+1)

    for i in range(M):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
        
    def func(start):
        q=[]
        heapq.heappush(q,(0,start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < distance:
                continue
            for i in graph[now]:
                cost = dist+i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
                    
    func(1)

    print(distance[-1])
    
    