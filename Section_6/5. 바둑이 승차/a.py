import sys

# 재귀 레벨 v, 현재 부분 집합의 무게 합 sum, 현재까지 모든 바둑이의 무게 합 tsum
def DFS(v, sum, tsum):
    global result
    if sum+(total-tsum) < result: return # 남은 바둑이를 모두 태운다 가정했을 때, 갱신하지 못한다면 return(시간 복잡도를 줄이기 위해)
    if sum > limit: return # 무게 제한을 넘겼다면 부분 집합 생성하지 않는다(시간 복잡도를 줄이기 위해)
    # 부분 집합 생성
    if v == -1:
        if sum > result: result = sum # 최대 무게 갱신
    else:
        DFS(v-1,sum+weight[v], tsum+weight[v]) # 인덱스 v의 바둑이를 태우는 경우
        DFS(v-1,sum, tsum+weight[v]) # 인덱스 v의 바둑이를 태우지 않는 경우

sys.stdin = open("in5.txt", 'r')

limit, n = map(int, input().split()) # 무게 제한 limit, 바둑이 수 n

weight = [] # n마리의 바둑이 무게 리스트
result = -1 # 가장 무거운 부분 집합의 무게 합

total = sum(weight) # n마리의 바둑이 무게 총합

for _ in range(n):
    weight.append(int(input()))

DFS(n-1,0,0)
print(result)
