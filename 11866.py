n,m = map(int, input().split())
circle_list = []
ans_list = []
number = 0
for i in range(n):
    circle_list.append(i+1)

def num_divide(num, circle_list_len):
    if (circle_list_len-1 < num):
        while (circle_list_len-1 < num):
            num = num % circle_list_len
    return num
    
for i in range(n):
    circle_list_len = len(circle_list)
    number = num_divide(number+(m-1) , circle_list_len)
    ans_list.append(circle_list[number])
    del circle_list[number]
print("<" + ", ".join(map(str,ans_list)) + ">")