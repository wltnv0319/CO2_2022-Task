import sys
from collections import Counter     # 2108번

# 2750번 : 수 정렬하기
def N_2750():
    N = int(input())
    Array = []

    for cnt_i in range(N):
        Array.append(int(input()))
        
    Array.sort()

    for cnt_j in range(N):
        print(Array[cnt_j])
        
# 2751번 : 수 정렬하기2
def N_2751():
    N = int(sys.stdin.readline())
    Array = []

    for cnt_i in range(N):
        Array.append(int(sys.stdin.readline()))
        
    Array.sort()

    for cnt_j in Array:
        print(cnt_j)
        
# 10989번 : 수 정렬하기3
def N_10989():
    N = int(input())

    Count = [0] * 10001

    for cnt_i in range(N):
        data = int(sys.stdin.readline())
        
        Count[data] = Count[data] + 1
        
    for cnt_i in range(10001):
        if Count[cnt_i] != 0:
            for cnt_j in range(Count[cnt_i]):
                print(cnt_i)
                
# 2108번 : 통계학
def N_2108():
    N = int(sys.stdin.readline())
    Array = []
    for i in range(N):
        Array.append(int(sys.stdin.readline()))
    Array.sort()
    number = Counter(Array).most_common()
    print(round(sum(Array) / N))
    print(Array[N // 2])
    if len(number) > 1:
        if number[0][1] == number[1][1]:
            print(number[1][0])
        else:
            print(number[0][0])
    else:
        print(number[0][0])
    print(Array[-1] - Array[0])
    
    
# 1427번 : 소트인사이드
def N_1427():
    data = input()

    Array = [int(N) for N in data]

    ordered_data = sorted(data, reverse=True)

    for N in ordered_data:
        print(N, end="")
    
# 11650번 : 좌표 정렬하기
def N_11650():
    data = sys.stdin.readline
    N = int(data())
    Array = []

    for cnt_i in range(N):
        [x, y] = map(int, data().split())
        Array.append([x, y])
        
    Sorted_Array = sorted(Array)

    for cnt_i in range(N):
        print(Sorted_Array[cnt_i][0], Sorted_Array[cnt_i][1])

# 11651번 : 좌표 정렬하기3
def N_11651():
    data = sys.stdin.readline
    N = int(data())
    Array = []

    for cnt_i in range(N):
        [x, y] = map(int, data().split())
        Array.append([y, x])
        
    Sorted_Array = sorted(Array)

    for cnt_i in range(N):
        print(Sorted_Array[cnt_i][1], Sorted_Array[cnt_i][0])

# 1181번 : 단어 정렬
def N_1181():
    Num_Word = int(input())
    Word_list = []

    for cnt_i in range(Num_Word):
        word = str(input())
        word_count = len(word)
        Word_list.append((word, word_count))

    #중복 삭제
    Word_list = list(set(Word_list))

    #단어 숫자 정렬 > 단어 알파벳 정렬
    Word_list.sort(key = lambda word: (word[1], word[0]))

    for word in Word_list:
        print(word[0])
        
# 10814번 : 나이순 정렬
def N_10814():
    data = sys.stdin.readline
    N = int(data())
    User_Array = []

    for cnt_i in range(N):
        User_Array.append(list(data().split()))
        
    User_Array.sort(key=lambda a:int(a[0]))

    for cnt_i in range(N):
        print(User_Array[cnt_i][0], User_Array[cnt_i][1])
        
# 18870번 : 좌표 압축
def N_18870():
    N = int(input())

    Coordinate_List = list(map(int, input().split()))

    Coordinate_Sorted = sorted(list(set(Coordinate_List)))

    Array = {Coordinate_Sorted[cnt_i]: cnt_i for cnt_i in range(len(Coordinate_Sorted))}

    for Coordinate in Coordinate_List:
        print(Array[Coordinate], end = ' ')