# 2798번 : 블랙잭
def N_2798():
    n, m = map(int,input().split())
    array = list(map(int, input().split()))
    card_sum = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                temp = array[k]+array[i]+array[j]
                if temp <= m:
                    card_sum.append(temp)
                    
    print(max(card_sum))
    
# 2231번 : 분해합
def N_2231():
    n = int(input())

    result = []

    for i in range(1, n):
        string = str(i)
        List = list(string)
        temp = i
        
        for j in range(len(List)):
            temp += int(List[j])
        
        if temp == n:
            result.append(i)

    if result == []:
        print(0)
    else:
        print(min(result))
    
# 7568번 : 덩치
def N_7598():
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]

    for i in array:
        result = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            result += 1
    
    print(result, end = " ")
    

# 1018번 : 체스판 다시 칠하기
def N_1018():
    n, m = map(int, input().split())
    Table = []
    Count = []

    for i in range(n):
        Table.append(input())
        
    for i in range(n-7):
        for j in range(m-7):
            temp_1 = 0
            temp_2 = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if (k+l)%2 ==0:
                        if Table[k][l] != 'W':
                            temp_1 += 1
                        if Table[k][l] != 'B':
                            temp_2 += 1
                    else:
                        if Table[k][l] != 'B':
                            temp_1 += 1
                        if Table[k][l] != 'W':
                            temp_2 += 1
            Count.append(min(temp_1, temp_2))
            
    print(min(Count))

# 1436번 : 영화감독 숌
def N_1436():
    n = int(input())
    Target = 666
    count = 0
    while True:
        if '666' in str(Target):
            count += 1
        if count == n:
            print(Target)
            break
        Target += 1