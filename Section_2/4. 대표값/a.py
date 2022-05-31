# N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, 
# N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
# 평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높은 점수를 가진 학생이 여러 명일 경우 
# 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

import sys
sys.stdin = open("in5.txt", 'r')

n = int(input()) # 학생 수
score = list(map(int, input().split()))

# sum = 0

# for stu in score:
#     sum += stu

# avg = round(sum(score) / n) # 학생 평균 점수, 소수 첫째자리까지만 표기

# 학생 평균 점수 반올림, round 함수는 round half even 방식이라 사용 안함

avg = sum(score) / n + 0.5
avg = int(avg)

dif = 100
ans = 0


# abs() 함수를 통해 절대값 반환가능

for stuNum in range(len(score)):
    if score[stuNum] >= avg: # 평균보다 점수가 높을 때
        if score[stuNum] - avg < dif: # 점수 차이가 똑같다면 갱신 안해준다(학생 번호가 가장 빠른 학생으로 갱신)
            dif = score[stuNum] - avg # 차이 갱신
            ans = stuNum # 학생 번호 갱신
        if score[stuNum] - avg == dif and score[stuNum] > score[ans]: # 평균과 가장 가까운 점수 중 점수가 더 높은 학생이 있다면
            dif = score[stuNum] - avg # 차이 갱신
            ans = stuNum # 학생 번호 갱신
    else: # 평균보다 점수가 낮을 때
        if avg - score[stuNum] < dif:
            dif = avg - score[stuNum] # 차이 갱신
            ans = stuNum # 학생 번호 갱신


print(avg, ans+1) # 평균, 평균에 가장 가까운 학생의 번호 출력
