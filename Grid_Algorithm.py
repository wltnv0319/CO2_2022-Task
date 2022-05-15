import sys

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