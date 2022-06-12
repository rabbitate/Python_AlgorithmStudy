# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열)이면 YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
# 단 회문을 검사할 때 대소문자를 구분하지 않습니다.

import sys

dif = abs(ord('a')-ord('A')) # 같은 알파벳이지만 대소문자가 다를 경우의 아스키 코드 차이값

def check(s):
    # for i in range(len(s)//2): # 문자열의 절반만 검사
    #     if s[i] != s[-1-i] and abs(ord(s[i]) - ord(s[-1-i])) != dif: # 같은 문자가 아니고, 대소문자 구분 없이 같은 문자가 아니라면
    #         print("NO") # 회문 문자열이 아니다
    #         break
    # else:
    #     print("YES")

    s = s.upper() # 대소문자 구별이 없으므로 모두 대문자로 변경 후

    if s == s[::-1]: # 회문의 슬라이싱과 같을 경우
        print("YES")
    else:
        print("NO")

sys.stdin = open("in5.txt", 'r')

n = int(input()) # 문자열의 개수 입력

for i in range(n):
    s = input()
    print("#%d" %(i+1), end=' ')
    check(s)
