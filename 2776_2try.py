import sys
input = sys.stdin.readline

T = int(input())
N = int(input())
note1 = list(map(int,input().split()))
note1 = sorted(note1)

for t in range(T):
    N = int(input())
    note2 = list(map(int,input().split()))

#binary search