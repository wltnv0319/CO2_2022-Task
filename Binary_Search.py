import sys

# 1920번 : 수 찾기
def N_1920():
    n = int(sys.stdin.readline())
    Number = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split()))

    for cnt_i in M_list:
        if cnt_i in Number:
            print(1)
        else:
            print(0)

# 10816번 : 숫자 카드2
def N_10816():
    data = sys.stdin.readline

    N = int(input())
    Number_list = list(map(int, data().split()))
    M = int(input())
    M_list = list(map(int, data().split()))
    temp = {}

    for cnt_i in Number_list:
        if cnt_i in temp:
            temp[cnt_i] += 1
        else:
            temp[cnt_i] = 1
            
    print(' '.join(str(temp[cnt_j]) if cnt_j in temp else '0' for cnt_j in M_list))
        
# 1654번 : 랜선 자르기
def N_1654():
    data = sys.stdin.readline

    N, M = map(int, data().split())
    lan = []

    for cnt_i in range(N):
        lan.append(int(input()))
        
    Min, Max = 1, max(lan)

    while Min <= Max:
        total = 0
        cut = (Min+Max) // 2
        
        for cnt_i in lan:
            total +=(cnt_i//cut)
            
        if total >= M:
            Min=cut+1
        else:
            Max = cut - 1
        
    print(Max)

# 2805번 : 나무 자르기
def N_2805():
    data = sys.stdin.readline

    N,M = map(int, data().split())
    Trees = list(map(int, data().split()))

    low, height = 0, max(Trees)
    while low <= height:
        cut = (low+height) // 2
        sum = 0
        
        for tree in Trees:
            if tree>cut:
                sum += tree - cut
                
        if sum >= M:
            low = cut + 1
        else:
            height = cut - 1
        
    print(height)
    
# 2110번 : 공유기 설치 (실패)
def N_2110():
    data = sys.stdin.readline

    N,M = map(int, data().split())
    wifi = []

    for cnt_i in range(N):
        wifi.append(int(data()))

    wifi.sort()

    Min, Max = 1, max(wifi)
    total = 0

    while Min <= Max:
        temp = wifi[0]
        mid = (Min+Max)//2
        count = 1
        
        for cnt_i in range(N):
            if wifi[cnt_i] >= temp+mid:
                temp = wifi[cnt_i]
                count += 1
                
        if count >= M:
            Min = mid+1
            total = mid
        else:
            Max = mid -1
            
    print(total)
    
# 12015번 : 가장 긴 증가하는 부분 수열2 (실패)
def N_12015():
    data = sys.stdin.readline

    N = int(data())
    N_list = list(map(int, data().split()))
    binary = [0]

    for cnt_i in N_list:
        if binary[-1] < cnt_i:
            binary.append(cnt_i)
        else:
            start, end = 0, len(binary)
            
            while start < end:
                mid = (start + end) //2
                
                if binary[mid] < cnt_i:
                    start = mid +1
                else:
                    end = mid
                    
            binary[end] = cnt_i
            
    print(len(binary[1:]))