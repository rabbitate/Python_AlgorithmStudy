# 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 교환 해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.
# 첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종 류가 주어지고, 그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
# 각 동전의 종류는 100원을 넘지 않는다.

import sys

# 현재 동전 금액 money, 동전 개수 합 sum 
def DFS(money, sum):
    global res, n
    if sum > res: return # 가장 적은 수의 동전이 필요하므로, 현재 동전 개수가 res보다 크다면 return
    if money < 0: return # 거스름돈을 넘는 금액은 return
    # 거슬러줬을 때
    elif money == 0:
        # 더 적은 수의 동전 개수로 갱신해줄 수 있다면
        if sum < res:
            res = sum
        return
    else:
        for i in range(0,n):
            DFS(money-coin[i],sum+1)

sys.stdin = open("in4.txt", 'r')

n = int(input()) # 동전의 개수
coin = list(map(int, input().split())) # 동전 리스트
m = int(input()) # 거스름돈

coin.sort(reverse=True) # 내림차순 정렬, 가장 큰 동전부터 적용해주기 위해

res = sys.maxsize # 거슬러 줄 동전의 최소 개수
DFS(m, 0)
print(res)
