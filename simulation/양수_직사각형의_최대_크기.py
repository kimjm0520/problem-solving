n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
ans=-1

def run(c,r,cnt_max):
    cnt=0
    for i in range(c,n):
        for j in range(r,m):
            p=False
            for k in range(c,i+1):
                if graph[k][j]<1:
                    p=True
                    break
            if p:
                break
            cnt=(i-c+1)*(j-r+1)
            if cnt>cnt_max:
                cnt_max=cnt
    return cnt_max


cnt_max=-1
for i in range(n):
    for j in range(m):
        cnt_max=run(i,j,cnt_max)
print(cnt_max)