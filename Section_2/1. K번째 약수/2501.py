import sys
# sys.stdin = open("in2.txt", "r")

p, q = map(int, input().split()) # 입력받은 값을 공백을 기준으로 분리 후, int형으로 변환

cnt = 0 # q번째 약수를 찾기 위한 변수

for i in range(1,p+1):
    if p % i == 0: # 약수라면 1을 추가
        cnt += 1
    if cnt == q:
        print(i)
        break
else: # for문이 정상적으로 종료되었다면 실행되는 for else 문
    print(0) # q번째 약수를 찾지 못했다면 0 출력
