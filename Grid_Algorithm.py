# 그리드 알고리즘

import sys

# 11047번 : 동전0
def N_11047():
    N, K = map(int, sys.stdin.readline().split())

    coin = []

    for cnt_i in range(N):
        coin.append(int(sys.stdin.readline()))
        
    temp = N-1
    count = 0

    while(True):
        if temp < 0 :
            break
        if K // coin[temp] >0:
            count += K // coin[temp]
            K = K % coin[temp]
        else:
            temp -= 1
            
    print(count)
    
# 1931번 : 회의실 배정
def N_1931():
    data = sys.stdin.readline

    N = int(data())

    meeting_time = []

    for cnt_i in range(N):
        M_start, M_end = map(int, data().split())
        meeting_time.append([M_start, M_end])
        
    meeting_time.sort(key = lambda x:(x[1],x[0]))

    count=1

    end_time = meeting_time[0][1]
    for cnt_i in range(1,len(meeting_time)):
        if meeting_time[cnt_i][0]>=end_time:
            count+=1
            end_time = meeting_time[cnt_i][1]
            
    print(count)
        
# 11399번 : ATM
def N_11399():
    input = sys.stdin.readline

    N = int(input())

    people = list(map(int, input().split()))
    people.sort()

    time = 0

    for cnt_i in range(1, N):
        people[cnt_i] += people[cnt_i-1]
        
    print(sum(people))

# 1541번 : 잃어버린 괄호
def N_1541():
    string = input().split('-')

    List = []

    for cnt_i in string:
        count = 0
        s = cnt_i.split('+')
        for cnt_j in s:
            count += int(cnt_j)
        List.append(count)

    answer = List[0]

    for cnt_i in List[1:]:
        answer -= cnt_i
        
    print(answer)
    
# 13305번 : 주유소
def N_13305():
    data = sys.stdin.readline

    N = int(data())

    road = list(map(int, data().split())) 
    oil = list(map(int, data().split())) 

    Min_oil_cost = 10000000000000

    result = 0
    min_result = 0

    for cnt_i, price_oil in enumerate(oil):

        if price_oil <= Min_oil_cost:
            result += Min_oil_cost * sum(road[min_result : cnt_i])
            Min_oil_cost = price_oil
            min_result = cnt_i

    if min_result != N-1:
        result += Min_oil_cost*sum(road[min_result :])

    print(int(result))
