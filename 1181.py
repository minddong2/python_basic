# n = int(input())
# input_list = []
# len_number_list = []


# for i in range(n):
#     input_list.append(input())


# for i in range(n):
#     len_number_list.append(len(inputd_list[i]))
# print(input_list)
# for i in range(n):
#     min_len = min(len_number_list)
#     len_number_list.remove(min_len)
#     if len(input_list[i]) <= min_len:
#         input_list.insert(0,input_list[i])

#         del input_list[i+1]
n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=lambda x : len(x))
for i in words:
    print(i)