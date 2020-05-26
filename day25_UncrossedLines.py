#hint - LCS(Dynamic Programming)
if __name__ == '__main__':
    n=int(input())
    m=int(input())
    A=list(map(int,input().split()))[:n]
    B=list(map(int,input().split()))[:m]
    c=0
    t=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if A[i-1]==B[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    print(t[n][m])
