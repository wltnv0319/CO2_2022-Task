# 누적합 (a~b)
# b까지의 누적합을 구한후 
# (a-1)까지의 누적합을 빼면 a부터 b까지의 누적합

import sys

# 11659번 : 구간 합 구하기 4
def N_11659():
    data = sys.stdin.readline

    N, M = map(int, data().split())

    number = list(map(int, data().split()))

    temp = [0]
    sum_N = 0

    for cnt_i in number:
        sum_N += cnt_i
        temp.append(sum_N)

    for cnt_j in range(M):
        A, B = map(int, data().split())
        print(temp[B] - temp[A-1])

# 2559번 : 수열
def N_2559():
    data = sys.stdin.readline

    N, K = map(int, data().split())

    array = list(map(int, data().split()))

    result = []
    result.append(sum(array[:K]))

    for cnt_i in range(N-K):
        result.append(result[cnt_i] - array[cnt_i] + array[K+cnt_i])
        
    print(max(result))
    
# 16139번 : 인간-컴퓨터 상호작용        (실패)
def N_16139():
    data = sys.stdin.readline

    String = data().rstrip()

    array = [[0]*26]

    array[0][ord(String[0])-97] = 1

    for cnt_i in range(1, len(String)):
        array[cnt_i][ord(String[cnt_i]) - 97] = 1
        for cnt_j in range(26):
            array[cnt_i][cnt_j] += array[cnt_i-1][cnt_j]
    
# 10986번 : 나머지 합
def N_10986():
    

# 11660번 : 구간 합 구하기 5
def N_11660():