import sys
k,n = map(int,sys.stdin.readline().split())
# k = 4 n = 11

arr = []
for i in range(k):
	arr.append(int(input()))
# arr = [802,743,457,539]

start = 1
end = max(arr)

while start <= end:
	count = 0
	mid = (start+end) // 2
	for i in arr:
		count += i // mid
	if count >= n:
		start = mid+1
	else:
		end = mid-1
	# print("count=",count,"start=",start,"end=",end,"mid=",mid)
print(end)