n = int(input())

members = []

for index in range(n):
    age , member  = input().split()
    members.append((int(age), member, index))

member_list = sorted(members, key = lambda x : (x[0], x[2]))
print(member_list)
for member in member_list:
    print(member[0],member[1])