n = int(input())
pattern_list = [[10],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]
for i in range(n):
    x,y = map(str,input().split())
    x_number = int(x[-1])
    y = int(y)
    index = y % len(pattern_list[x_number])
    answer = pattern_list[x_number][index-1]
    print(answer)