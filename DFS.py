import sys

# 2210번 : 숫자판 점프
def N_2210():
    def jump(x, y, num):
        if len(num) == 6:
            if num not in result:
                result.append(num)
            return
    
        dx=[1,-1,0,0]
        dy=[0,0,1,-1]
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=5 or ny<0 or ny>=5:
                continue
            else:
                jump(nx,ny,num+Table[nx][ny])
    
    Table = []
    
    for i in range(5):
        Table.append(list(map(str, input().split())))
    
    result = []
    
    for i in range(5):
        for j in range(5):
            jump(i, j, Table[i][j])
            
    print(len(result))
            

# 3187번 : 양치기 꿍 (실패)
def N_3187():
    data = sys.stdin.readline

    Burger = map(int, data().split())
    Side = map(int, data().split())
    Drink = map(int, data().split())

    burger = sorted(list(map(int, input().split())), reverse=True)
    side = sorted(list(map(int, input().split())), reverse=True)
    drink = sorted(list(map(int, input().split())), reverse=True)

    total = sum(burger)+sum(side)+sum(drink)

    min_set = min(len(burger), min(len(side)), min(len(drink)))
                
    cost = 0

    for _ in range(min_set):
        cost += (burger[0]+side[0]+drink[0]) * 0.9
        burger.pop(0)
        side.pop(0)
        drink.pop(0)
        
    for cnt_i in range(len(burger)):
        cost += burger[cnt_i]
        
    for cnt_i in range(len(side)):
        cost += side[cnt_i]
        
    for cnt_i in range(len(drink)):
        cost += drink[cnt_i]
        
    print(total)
    print(int(cost))