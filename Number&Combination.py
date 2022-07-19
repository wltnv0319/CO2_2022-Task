import sys
import math # 2609번 사용

# 5086번 : 배수와 약수
def N_5086():
    while True:
        X, Y = map(int, input().split())
        if X == 0 and Y == 0:
            break
        if Y % X == 0:
            print("factor")
        elif X % Y ==0:
            print("multiple")
        else:
            print("neither")

# 1037번 : 약수
def N_1037():
    Number = int(input())

    data = list(map(int, input().split()))

    Max = max(data)
    Min = min(data)

    Divisor = Max * Min

    print(Divisor)    
    
# 2609번 : 최대공약수와 최소공배수
def N_2609():
    import math

    X, Y = map(int, input().split())

    GCD = math.gcd(X,Y)
    LCM = math.lcm(X,Y)

    print(GCD)
    print(LCM)
    
# 1934번 : 최소공배수
def N_1934():
    data = int(input())

    for cnt_i in range(data):
        A, B = map(int, input().split())
        LCM = math.lcm(A, B)
        print(LCM)
    
# 2981번 : 검문     // 풀지 못 함
def N_2981():
    data = int(sys.stdin.readline())

    Number = int(input())

    Sort_Num = sorted(int(input()))
    
# 3036번 : 링
def N_3036():
    N = int(sys.stdin.readline())

    Ring = list(map(int, input().split()))

    for cnt_i in range(N-1):
        GCD = math.gcd(Ring[0], Ring[cnt_i+1])
        print(f"{Ring[0]//GCD}/{Ring[cnt_i+1]//GCD}")

# 11050번 : 이항 계수1
def N_11050():
    def binomial_coefficient(number):
        if number <= 1:
            return 1
        return number*binomial_coefficient(number-1)

    N, K = map(int, input().split())

    result = binomial_coefficient(N) // (binomial_coefficient(K)*binomial_coefficient(N-K))
    print(result)
    
# 11051번 : 이항 계수2
def N_11051():
    data = sys.stdin.readline()

    N, K = map(int, data().split())

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

# 9375번 : 패션왕 신해빈        // 못 품
def N_9375():
    data = sys.stdin.readline

    N = int(data())

    for cnt_i in range(N):
        clothes = {}

# 1676번 : 팩토리얼 0의 개수
def N_1676():
    Number = int(input())

    counter = 0

    while Number > 0:
        counter += Number // 5
        Number // 5
        
    print(counter)

# 2004번 : 조합 0의 개수
def N_2004():
    data = sys.stdin.readline

    N, M = map(int, data().split())

    def Cal_2(number):
        if number < 2:
            return 0
        counter = 0
        while number>=2:
            counter += number//2
            number = number//2
        return counter

    def Cal_5(number):
        if number<5:
            return 0
        counter = 0
        while number >= 5:
            counter += number//5
            number //=5
        return counter

    multiple_2 = Cal_2(N) - Cal_2(N-M) - Cal_2(M)
    multiple_5 = Cal_5(N) - Cal_5(N-M) - Cal_5(M)

    result = min(multiple_2, multiple_5)

    print(result)