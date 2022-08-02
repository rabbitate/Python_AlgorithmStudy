# 정보 왕국의 이웃 나라 외동딸 공주가 숲속의 괴물에게 잡혀갔습니다.
# 정보 왕국에는 왕자가 N명이 있는데 서로 공주를 구하러 가겠다고 합니다. 
# 정보왕국의 왕은 다음과 같은 방법으로 공주를 구하러 갈 왕자를 결정하기로 했습니다.
# 왕은 왕자들을 나이 순으로 1번부터 N번까지 차례로 번호를 매긴다. 
# 그리고 1번 왕자부터 N 번 왕자까지 순서대로 시계 방향으로 돌아가며 동그랗게 앉게 한다. 
# 그리고 1번 왕자부터 시 계방향으로 돌아가며 1부터 시작하여 번호를 외치게 한다. 
# 한 왕자가 K(특정숫자)를 외치면 그 왕자는 공주를 구하러 가는데서 제외되고 원 밖으로 나오게 된다. 
# 그리고 다음 왕자부터 다시 1부터 시작하여 번호를 외친다.
# 이렇게 해서 마지막까지 남은 왕자가 공주를 구하러 갈 수 있다.

from collections import deque
import sys

sys.stdin = open("in2.txt", 'r')

n, k = map(int, input().split())

prince = deque([i for i in range(1,n+1)]) # 1부터 n까지의 숫자를 담은 리스트를 deque로 변환

# prince에 왕자 한 명만 남을 때까지
while len(prince)!=1:
    for _ in range(k-1):
        prince.append((prince.popleft())) # 1번부터 k-1번 왕자는 append해준다
    prince.popleft() # k번 왕자 pop

print(prince[0]) # 남은 왕자 한 명 출력
