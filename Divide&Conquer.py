import sys
import math  #6549번

# 2630번 : 색종이 만들기
def N_2630():
    N = int(sys.stdin.readline())

    paper = [list(map(int, sys.stdin.readline().split()))for cnt_i in range(N)]

    blue = 0
    white = 0

    def solution(x, y, N):
        global blue, white
        color = paper[x][y]
        for cnt_i in range(x, x+N):
            for cnt_j in range(y, y+N):
                if color != paper[cnt_i][cnt_j]:
                    solution(x, y, N//2)
                    solution(x, y+N//2, N//2)
                    solution(x+N//2, y, N//2)
                    solution(x+N//2, y+N//2, N//2)
                    return
        if color == 0:
            white+=1
        else:
            blue+=1

    solution(0,0, N)
    print(white)
    print(blue)
    
# 1992번 : 쿼드트리     (틀림)
def N_1992():
    N = int(input())

    paper = [list(map(int, input())) for cnt_i in range(N)]

    def solution(x, y, N):
        temp = paper[x][y]
        for cnt_i in range(x, x+N):
            for cnt_j in range(y, y+N):
                if temp != paper[cnt_j][cnt_j]:
                    temp -= 1
                    break
        if temp == -1:
            print("(", end="")
            N = N//2
            solution(x,y,N)
            solution(x,y+N,N)
            solution(x+N,y,N)
            solution(x+N,y+N,N)
            print(")", end="")
        
        elif temp == 1:
            print(1, end = "")
        else:
            print(0, end = "")
    solution(0,0,N)

# 1780번 : 종이의 개수      (런타임 에러)
def N_1780():
    data = sys.stdin.readline

    def solution(x,y,N):
        temp = paper[x][y]
        for cnt_i in range(x,x+N):
            for cnt_j in range(y,y+N):
                if paper[cnt_i][cnt_j] != temp:
                    for cnt_k in range(3):
                        for cnt_l in range(3):
                            solution(x+cnt_k*(N//3),y+cnt_l*(N//3),N//3)
                    return

        if temp == -1:
            result[0] += 1
        elif temp == 0:
            result[1] += 1
        else:
            result[2] += 1

    N = int(data())
    paper = [list(map(int,data().split())) for cnt_i in range(n)]
    result = [0,0,0]

    solution(0,0,N)

    [print(answer) for answer in result]

# 1629번 : 곱셈
def N_1629():
    def Multiplication(A, B, C):
        if B == 1:
            return A % C
        elif B % 2 == 0:
            return (Multiplication(A,B//2,C)**2)%C
        else:
            return ((Multiplication(A,B//2,C)**2)*A)%C

    number = list(map(int, input().split()))
    print(Multiplication(number[0], number[1], number[2]))

# 11401번 : 이항 계수 3
def N_11401():
    data = sys.stdin.readline

    N, K = map(int, data().split())

    Number = 1000000007

    def factorial(N):
        n = 1
        for cnt_i in range(2, N+1):
            n = (n * cnt_i) % Number
        return n

    def square(N, K):
        if K == 0:
            return 1
        elif K == 1:
            return N
        temp = square(N, K//2)
        if K % 2:
            return temp * temp * N % Number
        else:
            return temp * temp % Number

    step_1 = factorial(N)
    step_2 = factorial(N-K) * factorial(K) % Number

    print(step_1 * square(step_2, Number-2) % Number)

# 2740번 : 행렬 곱셈
def N_2740():
    N,M=map(int,input().split())
    Mat_A=[list(map(int,input().split())) for cnt_i in range(N)]

    M,K=map(int,input().split())
    Mat_B=[list(map(int,input().split())) for cnt_i in range(M)]

    new_Mat=[[] for cnt_i in range(N)]
    count=0

    for cnt_n in range(N):
        for cnt_k in range(K):
            number=0
            for cnt_m in range(M):
                number +=Mat_A[cnt_n][cnt_m]*Mat_B[cnt_m][cnt_k]
            new_Mat[count].append(number)
    if count<M:
        count+=1

    for cnt_i in new_Mat:
        print(" ".join(list(map(str,cnt_i))))
    
# 10830번 : 행렬 제곱
def N_10830():
    data = sys.stdin.readline

    N, B = map(int, data().split())
    A = [[*map(int, data().split())] for cnt_i in range(N)]

    def multi(x, y):
        n = len(x)
        z = [[0]*n for cnt_i in range(n)]
        
        for row in range(n):
            for col in range(n):
                temp = 0
                for cnt_j in range(n):
                    temp += x[row][cnt_j] * y[cnt_j][col]
                z[row][col] = temp % 1000
        return z

    def square(A, B):
        if B == 1:
            for x in range(len(A)):
                for y in range(len(A)):
                    A[x][y] %= 1000
            return A
        
        temp = square(A, B//2)
        if B % 2:
            return multi(multi(temp, temp), A)
        else:
            return multi(temp, temp)

    result = square(A, B)
    for cnt_i in result:
        print(*cnt_i)
    
# 11444번 : 피보나치 수 6
def N_11444():
    data = sys.stdin.readline

    N = int(data())
    number = 1000000007

    def multi_by11444(A, B):
        n = len(A)
        Z = [[0]*n for cnt_i in range(n)]
        
        for row in range(n):
            for col in range(n):
                temp = 0
                for cnt_i in range(n):
                    temp += A[row][cnt_i] * B[cnt_i][col]
                Z[row][col] = temp % number           
        return Z

    def square_by11444(A, k):
        if k == 1:
            for x in range(len(A)):
                for y in range(len(A)):
                    A[x][y] %= number
            return A
        
        temp = square_by11444(A, k//2)
        if k % 2:
            return multi_by11444(multi_by11444(temp, temp), A)
        else:
            return multi_by11444(temp, temp)
        
    fibo_matrix = [[1, 1], [1, 0]]
    print(square_by11444(fibo_matrix, N)[0][1])
    
# 6549번 : 히스토그램에서 가장 큰 직사각형      (X)
def N_6549():
    
    rectangle = input()
    
    def max_rectangle():
        max_size = 0
        temp = []
        
        for cnt_i in range(N):
            index = cnt_i
            
            while temp and temp[-1][0] >= rectangle[cnt_i]:
                temp