# sum = 0
# v = [0] * 15
# n = int(input())

# def checkqueen(num,idx):
#     for i in range(0,idx):
#         if (num == v[i]):
#             return False
#         if (idx - i == v[i] - num):
#             return False
#         elif (idx - i == (v[i] - num) * (-1)):
#             return False
#     return True

# def n_queen(n,idx):
#     global sum
#     if(idx==n):
#         sum=sum+1
#         return
#     for i in range(1,n + 1):
#         if (v[i] == 0 and checkqueen(i,idx)):
#             v[idx] = i
#             n_queen(n,idx+1)
#             v[idx] = 0
#     if(idx == 0):
#         print(sum)

# n_queen(n,0)
# n = int(input())
# v = [0] * n

# def checkqueen(num, idx):
#     for i in range(idx):
#         if (v[i] == num):
#             return False
#         elif (idx - i == abs(v[i] - num)):
#             return False
#     return True

# def n_queen(n, idx):
#     if idx == n:
#         return 1
#     sum = 0
#     for i in range(1, n + 1):
#         if v[idx] == 0 and checkqueen(i, idx):
#             v[idx] = i
#             sum += n_queen(n, idx + 1)
#             v[idx] = 0
#     return sum

# print(n_queen(n, 0))



def dfs(n):
    global ans
    if n == N: #plus case 
        ans+=1
        return
        
    for i in range(N):
        if check_row[i]== check_column[n+i] == check_diagonal[n-i] == 0:
            check_row[i] = check_column[n+i] = check_diagonal[n-i] = 1 
            dfs(n+1)
            check_row[i] = check_column[n+i] = check_diagonal[n-i] = 0 

N = int(input())
ans = 0
check_row = [0] * N
check_column = [0] * (2*N)
check_diagonal = [0] * (2*N)
dfs(0)
print(ans)