import sys

# 10815번 : 숫자카드
def N_10815():
    N = int(input())
    Sang = list(map(int, input().split()))
    Sang.sort()

    M = int(input())
    M_list = list(map(int, input().split()))

    for i in range(M):
        low =0
        high = N-1
        
        while low <= high:
            mid = (low+high)//2
            
            if Sang[mid] == M_list[i]:
                print("1", end=" ")
                break
            elif Sang[mid] < M_list[i]:
                low = mid +1
            else:
                high = mid - 1
            
            if low > high:
                print("0", end=" ")
                break
            
# 14425번: 문자열 집합
def N_14425():
    input = sys.stdin.readline

    N, M = map(int, input().rstrip().split())
    word_S = set()
    counter = 0
    check = set()

    for i in range(N):
        word_S.add(input().rstrip())

    for j in range(M):
        temp = input().rstrip()
        
        if temp in word_S:
            counter += 1
            
    print(counter)
    
# 1620번 : 나는야 포켓몬 마스터 이다솜
def N_1620():
    N, M = map(int, input().split())
    dict = {}

    for i in range(1, N+1):
        pokemon = sys.stdin.readline().rstrip()
        dict[i] = pokemon
        dict[pokemon] = i
        
    for j in range(M):
        answer = sys.stdin.readline().rstrip()
        if answer.isalpha() == False:
            print(dict[int(answer)])
        else:
            print(dict[answer])
    
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
        
# 1764번 : 듣보잡
def N_1764():
    N, M = map(int, input().split())

    listen = []
    news = []
    result = 0

    for cnt_i in range(N): # 듣지 못한 사람
        listen.append(sys.stdin.readline().rstrip())
        
    for cnt_j in range(M): # 보도 못한 사람
        news.append(sys.stdin.readline().rstrip())

    List_sort = sorted(list(set(listen) & set(news)))

    print(len(List_sort))

    for cnt_k in range(len(List_sort)):
        print(List_sort[cnt_k])
    
# 1269번 : 대칭 차집합
def N_1269():
    A, B = map(int, input().split())

    A_list = list(map(int, input().split()))
    B_list = list(map(int, input().split()))

    counter = 0
    same = 0
    check = {}

    for cnt_i in A_list:
        check[cnt_i] = True

    for cnt_j in B_list:
        if check.get(cnt_j) == True:
            same += 1
        else:
            counter += 1
            
    print(counter + (A-same))
    
# 11478번 : 서로 다른 부분 문자열 개수
def N_11478():
    N = input()
    S = set(N)

    for cnt_i in range(len(N)+1):
        for cnt_j in range(cnt_i+1, len(N)+1):
            S.add(str(N[cnt_i:cnt_j]))
            
    print(len(S))