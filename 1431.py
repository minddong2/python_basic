# n = int(input())
# input_list = []
# number_list = [0] * n
# for i in range(n):
#     input_list.append(input())

# for i in range(n):
#     small_string = input_list[i]
#     j = len(small_string)
#     sum = 0
#     for h in range(j):
#         if small_string[h] >= '1' and small_string[h] <= '9':
#             sum += int(small_string[h])
#     number_list[i] = sum

# for i in range(0,n-1):
#     for j in range(i+1, n):
#         if len(input_list[i]) > len(input_list[j]):
#             number_list[i],number_list[j] = number_list[j],number_list[i]
#             input_list[i],input_list[j] = input_list[j], input_list[i]
#         elif len(input_list[i]) == len(input_list[j]):
#             if number_list[i] > number_list[j]:
#                 number_list[i],number_list[j] = number_list[j],number_list[i]
#                 input_list[i],input_list[j] = input_list[j], input_list[i]
#             elif number_list[i] == number_list[j]:
#                 for h in range(len(input_list[i])):
#                     if input_list[i][h] > input_list[j][h]:
#                         input_list[i],input_list[j] = input_list[j], input_list[i]
#                         break
#                     elif input_list[i][h] < input_list[j][h]:
#                         break
                
                    
# for ans in input_list:
#     print(ans)

n = int(input())
input_list = []
number_list = [0] * n
for i in range(n):
    input_list.append(input())

for i in range(n):
    small_string = input_list[i]
    j = len(small_string)
    sum = 0
    for h in range(j):
        if small_string[h] >= '1' and small_string[h] <= '9':
            sum += int(small_string[h])
    number_list[i] = sum

for i in range(0,n-1):
    for j in range(i+1, n):
        if len(input_list[i]) > len(input_list[j]):
            number_list[i],number_list[j] = number_list[j],number_list[i]
            input_list[i],input_list[j] = input_list[j], input_list[i]
        elif len(input_list[i]) == len(input_list[j]):
            if number_list[i] > number_list[j]:
                number_list[i],number_list[j] = number_list[j],number_list[i]
                input_list[i],input_list[j] = input_list[j], input_list[i]
            elif number_list[i] == number_list[j]:
                # for h in range(len(input_list[i])):
                    # if input_list[i][h] > input_list[j][h]:
                    #     input_list[i],input_list[j] = input_list[j], input_list[i]
                    #     break
                    # elif input_list[i][h] < input_list[j][h]:
                    #     break
                    if input_list[i] > input_list[j]:
                        number_list[i],number_list[j] = number_list[j],number_list[i]
                    
for ans in input_list:
    print(ans)
        