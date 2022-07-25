import sys

# 11051번 : 이항계수 2      (정수론 및 조합론 문제 8번)
def N_11051():
    N,K = map(int, sys.stdin.readline().split())
    dp = [1,1,2]
    
    for cnt_i in range(3, N+1):
        dp.append(dp[cnt_i-1]*cnt_i)
        
    print((dp[N]//(dp[N-K]*dp[K])%10007))
    
# 1010번 : 다리 놓기        (정수론 및 조합론 문제 9번)
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

# 24416번 : 알고리즘 수업 - 피보나치 수 1       (실패)
def N_24416():
    data = sys.stdin.readline
    
    def fibo(N):    # 재귀
        global counter_1
        counter_1 += 1
        
        if N ==1 or N==2:
            counter_1 -=1
            return 1
        else:
            return fibo(N-1) + fibo(N-2)
        
    def fibo_2(N):  # 동적 프로그래밍
        dp = [0] * 41
        dp[1], dp[2] = 1,1
        
        global counter_2
        
        for cnt_i in range(3, N+1):
            dp[cnt_i] = dp[cnt_i-1] + dp[cnt_i-2]
            counter_2 += 1
        return dp[N]
    
    counter_1, counter_2 = 0, 0
    
    N = int(data())
    fibo(N)
    fibo_2(N)
    result = counter_1+counter_2
    print(result)
        
# 9184번 : 신나는 함수 실행         (런타임 오버)
def N_9184():
    def w(a,b,c):
        if a<=0 or b<=0 or c<=0:
            return 1
        elif a>20 or b>20 or c>20:
            return w(20,20,20)
        if all(a<b, b<c):
            dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        else:
            dp[a][b][c] = w(a-1, b,c) +w(a-1, b-1,c)+w(a-1, b,c-1)-w(a-1,b-1,c-1)
        return dp[a][b][c]

    dp = [[[0 for cnt_i in range(21)] for cnt_j in range(21)] for cnt_k in range(21)]

    while True:
        a,b,c = map(int, input().split())
        
        if a==-1 and b==-1 and c==-1:
            break
        print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))

# 1904번 : 01타일
def N_1904():
    data= sys.stdin.readline

    def tile(N):
        dp = [0] * 1000001
        dp[1], dp[2] = 1,2
        
        for cnt_i in range(3, N+1):
            dp[cnt_i] = (dp[cnt_i-1] +dp[cnt_i -2]) % 15746
        return dp[N]

    N = int(data())
    print(tile(N))

# 9461번 : 파도반 수열
def N_9461():
    data = sys.stdin.readline

    def Triangle(N):
        dp = [0] * 101
        dp[1], dp[2], dp[3] = 1,1,1
        
        for cnt_i in range(4, N+1):
            dp[cnt_i]= dp[cnt_i-2]+dp[cnt_i-3]
        return dp[N]

    temp = int(input())
    for cnt_i in range(temp):
        N = int(input())
        print(Triangle(N))

# 1912번 : 연속합
def N_1912():
    N = int(sys.stdin.readline())

    if N > 1000000 or N <1:
        print("범위 오류")
    else:
        number_list = list(map(int, sys.stdin.readline().split()))
        if len(number_list) != N:
            print("오류")
        else:
            dp = [0] * N
            dp[0] = number_list[0]
            
            for cnt_i in range(1, N):
                dp[cnt_i] = max(number_list[cnt_i], number_list[cnt_i]+dp[cnt_i-1])
            print(max(dp))

# 1149번 : RGB 거리         (실패)
def N_1149():
    data = sys.stdin.readline
    N= int(data)

    dp= [list(map(int, data().split())) for cnt_i in range(N)]

    for cnt_i in range(1, N):
        dp[cnt_i][0] += min(dp[cnt_i-1][1], dp[cnt_i-1][2])
        dp[cnt_i][1] += min(dp[cnt_i-1][0], dp[cnt_i-1][2])
        dp[cnt_i][2] += min(dp[cnt_i-1][0], dp[cnt_i-1][1])

    print(min(dp[-1]))

# 1932번 : 정수 삼각형          (실패)
def N_1932():
    
    input = sys.stdin.readline
    N = int(input())
    dp = []
    
    for cnt_i in range(N):
        dp.append(list(map(int, input().split())))

    temp = 2

    for cnt_i in range(1,N):
        for cnt_j in range(temp):
            if cnt_j ==0:
                dp[cnt_i][cnt_j] = dp[cnt_i-1][cnt_j] + dp[cnt_i][cnt_j]
            elif cnt_i == cnt_j:
                dp[cnt_i][cnt_j] = dp[cnt_i-1][cnt_j-1] + N[cnt_i][cnt_j]
            else:
                dp[cnt_i][cnt_j] = max(dp[cnt_i-1][cnt_j-1], dp[cnt_i-1][cnt_j])+ dp[cnt_i][cnt_j]
        temp += 1
    print(max(dp[N-1]))

# 2579번 : 계단 오르기 
def N_2579():
    data = sys.stdin.readline

    def matter(N, stairs):
        if N<=2:
            return sum(stairs)
        
        dp = [0]* 301
        dp[0] = stairs[0]
        dp[1] = stairs[0]+stairs[1]
        dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
        
        for cnt_i in range(3, N):
            dp[cnt_i]= max(dp[cnt_i-3] + stairs[cnt_i-1] + stairs[cnt_i], dp[cnt_i-2]+stairs[cnt_i])
            
        return dp[N-1]

    N = int(data())
    stairs = [int(data()) for cnt_k in range(N)]
    print(matter(N,stairs))

# 1463번 : 1로 만들기
def N_1463():
    def Make_1(X):
        for cnt_i in range(2, X+1):
            dp[cnt_i] = dp[cnt_i-1] + 1
            
            if (cnt_i%2==0) and (dp[cnt_i] > dp[cnt_i//2] +1):
                dp[cnt_i] = dp[cnt_i//2] + 1
            if (cnt_i%3==0) and (dp[cnt_i]>dp[cnt_i//3]+1):
                dp[cnt_i] = dp[cnt_i//3]+1
        return dp[X]

    X = int(sys.stdin.readline())

    dp = [0] * (X+1)

    print(Make_1(X))

# 10844번 : 쉬운 계단 수        (실패)
def N_10844():
    data = sys.stdin.readline
    N = int(data())
    dp = [[0]*10 for cnt_i in range(101)]

    for cnt_i in range(1,10):
        dp[1][cnt_i] = 1

    # Pass (잘 모르겠다.)

    print(sum(dp[N]) % 1000000000)

# 2156번 : 포도주 시식          (실패)
def N_2156():
    def Drink(wine):
        if N == 1:
            dp[0] = wine[0]
        elif N == 2:
            dp[0] = wine[0]
            dp[1] = wine[0]+wine[1]
        else:
            dp[0] = wine[0]
            dp[1] = wine[0]+wine[1]
            dp[2] = max(dp[1], wine[2]+ wine[0], wine[2]+wine[1])
        
        for cnt_i in range(3, N):
            dp[cnt_i] = max(max(wine[cnt_i]+ wine[cnt_i-1]+wine[cnt_i-3], wine[cnt_i]+dp[cnt_i-2]), dp[cnt_i-1])
            
        return dp[N-1]

    N = int(sys.stdin.readline())
    wine = [int(sys.stdin.readline()) for cnt_i in range(N)]
    dp = [0] * N

    print(Drink(wine))

# 11053번 : 가장 긴 증가하는 부분 수열
def N_11053():
    def longest_sequence(A):
        for cnt_i in range(N):
            for cnt_j in range(cnt_i):
                if A[cnt_i] > A[cnt_j] and dp[cnt_i] < dp[cnt_j]:
                    dp[cnt_i] = dp[cnt_j]
            dp[cnt_i] +=1
        return max(dp)

    N = int(sys.stdin.readline())
    A = list(map(int, input().split()))
    dp = [0] * N

    print(longest_sequence(A))

# 11054번 : 가장 긴 바이토닉 부분 수열      (실패)
def N_11054():
    data = sys.stdin.readline

    N= int(data())
    A = list(map(int, data().split()))
    dp = [0]*N

    def bitonic_subsequence(N):
        dp

# 2565번 : 전깃줄           (실패)
def N_2565():
    N = int(sys.stdin.readline().strip())

    power_cord = []
    for cnt_i in range(N):
        A, B = map(int, sys.stdin.readline().split())
        power_cord.append(A,B)
    power_cord.sort()    

    dp = [1 for cnt_i in range(N)]

    for cnt_i in range(N):
        for cnt_j in range(cnt_i):
            if power_cord[cnt_i][1] > power_cord[cnt_j][1]:
                dp[cnt_i] = max(dp[cnt_i], dp[cnt_j]+1)

    print(N-max(dp))

# 9251번 : LCS           (실패)
def N_9251():
    data = sys.stdin.readline

    sequence_1, sequence_2 = data.strip(), data.strip()
    len_1, len_2 = len(sequence_1), len(sequence_2)

    dp = [[0]*(len_2+1) for cnt_i in range(len_1+1)]

    for cnt_i in range(1, len_1+1):
        for cnt_j in range(1, len_2+1):
            if sequence_1[cnt_i-1] == sequence_2[cnt_j-1]:
                dp[cnt_i][cnt_j] = dp[cnt_i-1][cnt_j-1] +1
            else:
                dp[cnt_i][cnt_j] = max(dp[cnt_i][cnt_j-1], dp[cnt_i-1][cnt_j])
                
    print(dp[cnt_i-1][cnt_j-1])

# 12865번 : 평범한 배낭
def N_12865():
    N,K = map(int, sys.stdin.readline().split())

    dp = [[0] * (K+1) for cnt_i in range(N+1)]

    for cnt_i in range(1, N+1):
        W,V = map(int, input().split())
        for cnt_j in range(1, K+1):
            if W > cnt_j:
                dp[cnt_i][cnt_j] = dp[cnt_i-1][cnt_j]
            else:
                dp[cnt_i][cnt_j] = max(dp[cnt_i-1][cnt_j], dp[cnt_i-1][cnt_j-W] +V)
    print(dp[N][K])