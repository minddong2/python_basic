N,M = map(int, input().split())
answer_list = []
small_list = []

def dfs(len,small_list):
    if len == M:
        answer_list.append(small_list)
        return
    for i in range(1, N+1):
        dfs(len+1, small_list+[i])
dfs(0, [])
for i in answer_list:
    print(*i)
