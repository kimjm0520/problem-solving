n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
cnt_max=0

def can(c1,r1):
    if c1<0 or c1>=n or r1<0 or r1>=m:
        return False
    return True

def model1(c1,r1):
    global cnt_max
    if can(c1-1,r1) and can(c1,r1) and can(c1,r1+1):
        cnt=graph[c1-1][r1]+graph[c1][r1]+graph[c1][r1+1]
        cnt_max=max(cnt,cnt_max)

def model2(c1,r1):
    global cnt_max
    if can(c1+1,r1) and can(c1,r1) and can(c1,r1+1):
        cnt=graph[c1+1][r1]+graph[c1][r1]+graph[c1][r1+1]
        cnt_max=max(cnt,cnt_max)

def model3(c1,r1):
    global cnt_max
    if can(c1+1,r1) and can(c1,r1) and can(c1,r1-1):
        cnt=graph[c1+1][r1]+graph[c1][r1]+graph[c1][r1-1]
        cnt_max=max(cnt,cnt_max)

def model4(c1,r1):
    global cnt_max
    if can(c1-1,r1) and can(c1,r1) and can(c1,r1-1):
        cnt=graph[c1-1][r1]+graph[c1][r1]+graph[c1][r1-1]
        cnt_max = max(cnt,cnt_max)

def model5(c1,r1):
    global cnt_max
    if can(c1-1,r1) and can(c1,r1) and can(c1+1,r1):
        cnt=graph[c1-1][r1]+graph[c1][r1]+graph[c1+1][r1]
        cnt_max=max(cnt,cnt_max)

def model6(c1,r1):
    global cnt_max
    if can(c1,r1-1) and can(c1,r1) and can(c1,r1+1):
        cnt=graph[c1][r1-1]+graph[c1][r1]+graph[c1][r1+1]
        cnt_max=max(cnt,cnt_max)
    
for i in range(n):
    for j in range(m):
        model1(i,j)
        model2(i,j)
        model3(i,j)
        model4(i,j)
        model5(i,j)
        model6(i,j)
print(cnt_max)