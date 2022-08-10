# 현수는 영어로 시는 쓰는 것을 좋아합니다.
# 현수는 시를 쓰기 전에 시에 쓰일 단어를 미리 노트에 적어둡니다.
# 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다.
# 첫 번째 줄에 시에 쓰지 않은 한 개의 단어를 출력한다.

import sys

sys.stdin = open("in5.txt", 'r')

n = int(input())
note = {} # 단어와 사용 횟수를 저장하는 딕셔너리, note = dict()도 가능하다

# 단어와 단어 사용 횟수를 초기화
for _ in range(n):
    word = input()
    note[word] = 0 # 사용 횟수를 0으로 초기화

# 단어 사용
for _ in range(n-1):
    used_word = input()
    note[used_word] += 1 # 사용 횟수 1 증가

for key, value in note.items():
    # 사용 횟수(value)가 0이라면 출력
    if value == 0:
        print(key)
        break
