n=int(input())
graph=[list(map(int,input().split())) for _ in range(n)]

def can(c,r):
    if c<0 or c>=n or r<0 or r>=n:
        return False
    return True

def run1(c,r):
    cnt1=0
    p=False
    while can(c,r):
        c-=1
        r+=1
        cnt1+=1
    while (not p) and cnt1>1:
        c+=1
        r-=1
        cnt1-=1
        if can(c-1,r-1):
            p=True
            return p,cnt1
    return p,cnt1
        
def run2(c,r):
    cnt2=0
    p=False
    while can(c,r):
        c-=1
        r-=1
        cnt2+=1
    while (not p) and cnt2>1:
        c+=1
        r+=1
        cnt2-=1
        if can(c+1,r-1):
            p=True
            return p,cnt2       
    return p,cnt2

def case1(c,r,ans,cnt1):
    p=False
    while can(c,r) and cnt1:
        ans+=graph[c][r]
        c-=1
        r+=1
        cnt1-=1
    if can(c-1,r-1):
        p=True
        return c,r,ans,p       
    return c,r,ans,p

def case2(c,r,ans,cnt2):
    p=False
    while can(c,r) and cnt2:
        ans+=graph[c][r]
        c-=1
        r-=1
        cnt2-=1
    if can(c+1,r-1):
        p=True
        return c,r,ans,p       
    return c,r,ans,p

def case3(c,r,ans,cnt1):
    p=False
    while can(c,r) and cnt1:
        ans+=graph[c][r]
        c+=1
        r-=1
        cnt1-=1
    if can(c+1,r+1):
        p=True
        return c,r,ans,p       
    return c,r,ans,p

def case4(c,r,c1,r1,ans):
    p=False
    while can(c,r) and (c!=c1 and r!=r1):
        ans+=graph[c][r]
        c+=1
        r+=1
    if c==c1 and r==r1:
        p=True
    return c,r,ans,p   


def qua(c,r,cnt1,cnt2):
    p=True
    c1,r1=c,r
    ans=0
    for i in range(1,5):
        if not p:
            return 0
        if i==1:
            c,r,ans,p=case1(c,r,ans,cnt1)
            
        elif i==2:
            c,r,ans,p=case2(c,r,ans,cnt2)
            
        elif i==3:
            c,r,ans,p=case3(c,r,ans,cnt1)
            
        elif i==4:
            c,r,ans,p=case4(c,r,c1,r1,ans)
            
    if not p:
        return 0
    return ans

ans_max=0

for i in range(n):
    for j in range(n):
        p1,cnt1=run1(i,j)
        if p1:
            for col in range(1,cnt1+1):
                p2,cnt2=run2(i-col,j+col)
                if p2:
                    for row in range(1,cnt2+1):
                        ans=qua(i,j,col,row)
                        if ans_max<ans:
                            ans_max=ans

        
print(ans_max)