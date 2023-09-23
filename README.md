# python_basic
N,M = map(int, input().split())
answer_list = []
check_list = [0] * (N+1)

def dfs(n, small_list):
    if small_list = M:
        answer_list + small_list
        return
    for i in range(1, N+1)
        if check_list[i] == 0:
            check_list[i] = 1
            dfs(n+1, small_list + [i])
            check_list[i] = 0
for i in answer_list:
    print(*i)