import sys
from collections import deque

# 18258번 : 큐2 
def N_18258():
    N = int(sys.stdin.readline())

    Queue = deque()

    for cnt_i in range(N):
        temp = sys.stdin.readline().split()
        
        if temp[0] == "push":
            Queue.append(temp[1])
            
        elif temp[0] == 'pop':
            if not Queue:
                print(-1)
            else:
                print(Queue.popleft())

        elif temp[0] == 'size':
            print(len(Queue))
            
        elif temp[0] == 'empty':
            if not Queue:
                print(1)
            else:
                print(0)
                
        elif temp[0] == 'front':
            if not Queue:
                print(-1)
            else:
                print(Queue[0])
                
        elif temp[0] == 'back':
            if not Queue:
                print(-1)
            else:
                print(Queue[-1])
    
    
# 2164번 : 카드2 
def N_2164():
    N = int(sys.stdin.readline())
    Card = deque()

    for cnt_i in range(1, N + 1):
        Card.append(cnt_i)

    while len(Card) != 1:
        Card.popleft()
        Card.append(Card.popleft())

    print(Card[0])
    
    
# 11866번 : 요세푸스 문제0      (틀림)
def N_11866():
    data = sys.stdin.readline
    N, K = map(int, data().split())

    Circle = deque([cnt_i for cnt_i in range(1, N+1)])

    Remove_People = []

    while Circle:
        Circle.rotate(-(K-1))
        Remove_People.append(Circle.popleft())
        
    print('<{", ".join(map(str,Remove_People))}>')

# 1966번 : 프린터 큐        (시간 초과)
def N_1966():
    data = sys.stdin.readline

    test_case = int(data())

    for cnt_i in range(test_case):
        N, index = map(int, data().split())
        Queue = deque(map(int,data().split()))
        index_queue = deque(range(0, N))
        
        temp = 0
        
        while Queue:
            if Queue[0] == max(Queue):
                temp += 1
                Queue.popleft()
                
                if index_queue.popleft() == index:
                    print(temp)
                    break
                else:
                    Queue.rotate(-1)
                    index_queue.rotate(-1)


# 10866번 : 덱      (틀림)
def N_10866():
    data = sys.stdin.readline

    Deque = deque()
    N = int(data())

    for cnt_i in range(N):
        temp = data().split()
        
        if temp[0] =="push_front":
            Deque.appendleft(temp[1])
        
        elif temp[0] == "push_back":
            Deque.append(temp[1])
        
        elif temp[0] == "pop_front":
            if Deque:
                print(Deque[0])
                Deque.popleft()
            else:
                print("-1")
                
        elif temp[0] == "pop_back":
            if Deque:
                print(Deque[len(Deque) -1])
                Deque.pop()
            else:
                print("-1")
                
        elif temp[0] == "empty":
            if Deque:
                print("0")
            else:
                print("1")
        
        elif temp[0] == "front":
            if Deque:
                print(Deque[0])
            else:
                print("-1")
                
        elif temp[0] == "back":
            if Deque:
                print(Deque[len(Deque) - 1])
            else:
                print("-1")


# 1021번 : 회전하는 큐
def N_1021():
    N, K = map(int, input().split())
    
    Queue = deque([cnt_i for cnt_i in range(1, N+1)])
    
    array = list(map(int, input().split()))
    
    count = 0
    
    for cnt_i in array:
        while True:
            if Queue[0] == cnt_i:
                Queue.popleft()
                break
            else:
                if Queue.index(cnt_i) <= len(Queue) // 2:
                    Queue.rotate(-1)
                    count += 1
                else:
                    Queue.rotate(1)
                    count += 1
    print(count)
    

# 5430번 : AC       (틀림)
def N_5430():
    data = sys.stdin.readline
    N = int(data())

    for cnt_i in range(N):
        Function = list(data())        # 명령 함수
        Number = int(data())
        
        if Number == 0:
            array = data()
            if 'D' in Function: # 길이가 0인데 D가 있을 경우 에러 발생
                print("error")
                continue
            else: # 길이가 0인데 D가 없을 경우에는 []출력
                print("[]") 
                continue
        array = list(input()[1:-2].split(',')) # 앞 뒤 []을 잘라주고 ,로 나눠준다.
        
        Reverse = False # reverse 여부
        start, end = 0,0 # index 선언
        
        for index in Function[:-1]:
            if index=="R":
                Reverse = not Reverse
            else:
                if Number == 0:
                    print("error")
                    break
                Number -= 1
                if Reverse:
                    end += 1
                else:
                    start += 1
        else:
            if Number:
                array.reverse()
                if start == 0:
                    array = array[end:]
                else: 
                    array = array[end:-start]
            else:
                if end == 0: 
                    array = array[start:]
                else: 
                    array = array[start:-end]
                        
            print("["+",".join(array)+"]")