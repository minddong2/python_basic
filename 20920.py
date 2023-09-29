import sys
N, M = map(int, sys.stdin.readline().split())
word_cnt = dict()

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    if not word_cnt.get(word):
        word_cnt[word] = 1
    else:
        word_cnt[word] += 1

word_list = word_cnt.keys()
print(word_list)
word_list = sorted(word_list, key=lambda x: (-word_cnt[x], -len(x), x))
for word in word_list:
    print(word)