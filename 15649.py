# from itertools import permutations
# n,m = map(int, input().split())
# answer_list = []

# for i in range(1,n+1):
#     answer_list.append(i)

# for i in list(permutations(answer_list,m)):
#     for j in i:
#         print(j, end=' ')
#     print()

# N,M = map(int, input().split())
# def dfs(n, lst):
#  #finish condition(about n) and answer print
 
#     if n == M:
#         answer_list.append(lst)
#         return
#     for j in range(1, N+1):
#         if v[j] == 0:
#             v[j] = 1
#             dfs(n+1, lst+[j])
#             v[j] = 0
# answer_list = []
# v = [0] * (N+1) #1 ~ n+1 duplication check, visited[0]4 

# dfs(0, [])
# for lst in answer_list:
#     print(*lst)

N,M = map(int, input().split())
answer_list = []
check_list = [0] * (N+1)

def dfs(n, small_list):
    if n == M:
        answer_list.append(small_list)
        return
    for i in range(1, N+1):
        if check_list[i] == 0:
            check_list[i] = 1
            dfs(n+1, small_list + [i])
            check_list[i] = 0
dfs(0, [])
for i in answer_list:
    print(*i)