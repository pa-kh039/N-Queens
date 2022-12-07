def colcheck(n,x,y,l):
    for i in range(x):
        if(l[i][y]==1):
            return False
    return True

def lcheck(n,x,y,l):
    for i in range(x):
        for j in range(y+1,n):
            if(l[i][j] == 1 and x-i==j-y):
                return False
    return True

def rcheck(n,x,y,l):
    for i in range(x):
        for j in range(y):
            if l[i][j] == 1 and x-i==y-j:
                return False
    return True
                
def diagcheck(n,x,y,l):
    return lcheck(n,x,y,l) and rcheck(n,x,y,l)

def check(n,x,y,l):
    return colcheck(n,x,y,l) and diagcheck(n,x,y,l)
         
def nQueen(n,x,l):
    if(x==n):
        for x1 in range(n):
            for y1 in range(n):
                print(l[x1][y1],end=" ")
        print()
        return
    for y in range(n):
        if(check(n,x,y,l)):
            l[x][y]=1
            nQueen(n,x+1,l)
            l[x][y]=0
    return

n = int(input())
# d={}
# for i in range(n):
#     d[i]=-1    # key :x , value: y
l=[[0 for i in range(n)] for j in range(n)]
nQueen(n,0,l)
# ---------------------------------------------------------------------------------------------------



