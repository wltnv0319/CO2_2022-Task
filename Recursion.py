import sys
input = sys.stdin.readline

# 10872번 : 팩토리얼
def N_10872():
    n = int(input())

    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n-1)
        
    print(factorial(n))
    
# 10870번 : 피보나치 수 5
def N_10870():
    n = int(input())

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1)+fibonacci(n-2)
        
    print(fibonacci(n))
    
# 17478번 : 재귀함수가 뭔가요?          실패
def N_17478():
    n = int(input())

    def recursion_ftn(n,m):
        print("____"*m+'"재귀함수가 뭔가요?"')
        if n == 0:
            print("____"*m+'"재귀함수는 자기 자신을 자신을 호출하는 함수라네"')
            return answer(m)
        print("____"*m+'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어."')
        print("____"*m+'"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."')
        print("____"*m+'"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        return recursion_ftn(n-1, m+1)

    def answer(n):
        if n<0:
            return
        print("____"*n+'라고 답변하였지.')
        return answer(n-1)

    print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
    recursion_ftn(n,0)
    
# 2447번 : 별 찍기 - 10         런타임 에러
def N_2447():
    n = int(input())

    def star(n):
        if n ==3:
            return['***', '* *', '***']
        array = star(1//3)
        dot = []
        
        for i in array:
            dot.append(i*3)
        
        for j in array:
            dot.append(i+' '*(1//3)+i)
            
        for k in array:
            dot.append(i*3)
        return dot

    print('\n'.join(star(n)))

# 11729번 : 하노이 탑 이동 순서         실패
def N_11729():
    def hanoi_tower(n, start, end, mid):
        if n < 2: 
            print(start, end) 
            return
        
        hanoi_tower(n-1, start, mid, end) 
        print(start, end) 
        
        hanoi_tower(n-1, mid, end, start)
        
    n = int(input()) 
    print((n**2)-1) 
    hanoi_tower(n, 1, 3, 2)