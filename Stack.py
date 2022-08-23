import sys

# 10828번 : 스택
def N_10828():
    data = sys.stdin.readline
    N = int(data())
    stack = []

    def push(x):
        stack.append(x)
        
    def pop():
        return stack.pop() if stack else -1
            
    def size():
        return len(stack)

    def empty():
        return 0 if stack else 1

    def top():
        return stack[-1] if stack else -1

    for cnt_i in range(N):
        action = data().split()
        temp = action[0]
        
        if temp == "push":
            push(action[1])
            
        elif temp == "pop":
            print(pop())
            
        elif temp == "size":
            print(size())
            
        elif temp == "empty":
            print(empty())
            
        elif temp == "top":
            print(top())

# 10773번 : 제로
def N_10773():
    data = sys.stdin.readline

    K = int(data())

    stack = []

    for cnt_i in range(K):
        number = int(data())
        if number == 0:
            stack.pop()    
        else:
            stack.append(number)

    print(sum(stack))

# 9012번 : 괄호
def N_9012():
    data = sys.stdin.readline

    T = int(data())
    
    for cnt_i in range(int(input())):
        given_string = input()
        stack = []
        
        for ch in given_string:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if not stack or stack[-1] != "(":
                    stack.append(")")
                    break

                stack.pop()

        print("YES" if not stack else "NO")

# 4949번 : 균형잡힌 세상        (틀림)
def N_4949():
    data = sys.stdin.readline

    while True:
        word = data().rstrip()
        
        if word == '.':
            break
            
        stack = []
        balance = True     # 균형이 맞으면 True, 틀리면 False
        
        for ch in word:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    balance = False
                    break
                    
            elif ch == '[':
                stack.append(ch)
            elif ch == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    balance = False
                    break

    if balance == False or stack:
        print('NO')
    elif not stack:
        print('YES')

# 1874번 : 스택 수열
def N_1874():
    data = sys.stdin.readline

    N = int(data())

    stack = []
    target = []
    Action = True

    pos = 1

    for cnt_i in range(N):
        number = int(data())
        
        while pos <= number:
            stack.append(pos)
            target.append('+')
            pos += 1
            
        if stack[-1] == number:
            stack.pop()
            target.append('-')
            
        else:
            Action = False
    
    if not Action:
        print("NO")
    else:
        for cnt_i in target:
            print(cnt_i)

# 17298번 : 오큰수
def N_17298():
    data = sys.stdin.readline

    N = int(data())
    array= list(map(int, data().split()))

    target = [-1 for cnt_i in range(N)]
    stack = []

    for cnt_i in range(N):
        try:
            while array[stack[-1]] < array[cnt_i]:
                target[stack.pop()] = array[cnt_i]
        
        except:
            pass
        
        stack.append(cnt_i)

    for cnt_i in range(N):
        print(target[cnt_i], end=" ")