n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]

def visit_cre():
    return [[0 for _ in range(m)] for _ in range(n)]

def graph_sum(c1,r1,c2,r2):
    cnt=0
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            cnt+=graph[i][j]
    return cnt

def visit_jud(c1,r1,c2,r2,visit): #2번째 맵의 좌표
    p=True
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            if visit[i][j]==1:
                p=False
                return p
    return p

def visit_map(c1,r1,c2,r2): #1번쨰 맵의 좌표
    visit=visit_cre()
    for i in range(c1,c2+1):
        for j in range(r1,r2+1):
            visit[i][j]=1
    return visit

def sub_graph(c1,r1,c2,r2):
    visit=visit_map(c1,r1,c2,r2)
    cnt=graph_sum(c1,r1,c2,r2)
    cnt_max=-9999999999999999999999
    for i in range(n):
        for j in range(m):
            for k in range(i,n):
                for l in range(j,m):
                    if visit_jud(i,j,k,l,visit):
                        cnt_max=max(cnt_max,cnt+graph_sum(i,j,k,l))
    return cnt_max

cnt_max=-9999999999999999999
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                cnt_max=max(cnt_max,sub_graph(i,j,k,l))
print(cnt_max) 