n,m,q=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def can(r):
    if r<0 or r>=n:
        return False
    return True

def wind(r,direction):
    if direction=='L':
        now=graph[r][-1]
        for i in range(m-1,0,-1):
            graph[r][i]=graph[r][i-1]
        graph[r][0]=now
    elif direction=='R':
        now=graph[r][0]
        for i in range(0,m-1):
            graph[r][i]=graph[r][i+1]
        graph[r][-1]=now

def spread_down(r,direction):
    if direction=='R':
        d="L"
    else:
        d='R'
    p=False
    for i in range(m):
        if can(r+1) and graph[r][i]==graph[r+1][i]:
            p=True
            return p,d,r+1
    return p,direction,r+1

def spread_up(r,direction):
    if direction=='R':
        d="L"
    else:
        d='R'
    p=False
    for i in range(m):
        if can(r-1) and graph[r][i]==graph[r-1][i]:
            p=True
            return p,d,r-1
    return p,direction,r-1

for _ in range(q):
    r,direction=input().split()
    r=int(r)-1
    wind(r,direction)

    p,direction_down,r_down = spread_down(r,direction)
    while p:
        wind(r_down, direction_down)
        p,direction_down,r_down = spread_down(r_down, direction_down)
    
    p,direction_up,r_up = spread_up(r,direction)
    while p:
        wind(r_up, direction_up)
        p,direction_up,r_up = spread_up(r_up,direction_up)

for i in range(n):
    for j in range(m):
        print(graph[i][j],end=' ')
    print()
