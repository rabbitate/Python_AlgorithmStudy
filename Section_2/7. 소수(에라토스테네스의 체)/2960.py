n, k = map(int, input().split())

list = [0] * (n + 1)

erase = 0 # 지운 횟수

for i in range(2,n+1):
    if list[i] == 0: # 소수라면
        for j in range(i,n+1,i): # 소수와 소수의 배수 둘 다 지워준다(에라토스테네스 체와의 차이점)
            if list[j] == 0: # 지우지 않았다면
                list[j] = 1
                erase += 1
            if erase == k:
                print(j)
                break
    if erase == k:
        break
