# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 그 구성이 일치하는 두 단어다.
# 예를 들면 AbaAeCe 와 baeeACA 는 알파벳을 나열 순서는 다르지만 그 구성을 살펴보면 A(2), a(1), b(1), C(1), e(2)로 알파벳과 그 개수가 모두 일치합니다. 
# 즉 어느 한 단어를 재배열하면 상대편 단어가 될 수 있는 것을 아나그램이라 합니다.
# 길이가 같은 두 개의 단어가 주어지면 두 단어가 아나그램인지 판별하는 프로그램을 작성하세요. 아나그램 판별시 대소문자가 구분됩니다.
# 두 단어가 아나그램이면 “YES"를 출력하고, 아니면 ”NO"를 출력합니다.

import sys

sys.stdin = open("in5.txt", 'r')

anagram = dict() # 알파벳(key)의 개수(value)를 저장하는 딕셔너리

s1 = input() # 비교 문자열 1
s2 = input() # 비교 문자열 2

for a in s1:
    # anagram[a] = anagram.get(a, 0) + 1, 존재하지 않는 key로 가져올 경우 0을 가져온 후 1을 더해줌
    try:
        anagram[a] += 1 # 해당하는 알파벳의 개수 증가
    # 딕셔너리에 없는 알파벳이 온 경우 1로 초기화
    except KeyError as e:
        anagram[a] = 1

for a in s2:
    # anagram[a] = anagram.get(a, 0) - 1
    try:
        anagram[a] -= 1 # 해당하는 알파벳의 개수 감소
    # 딕셔너리에 없는 알파벳이 온 경우 1로 초기화
    except KeyError as e:
        anagram[a] = 1 

for i in anagram.values():
    # anagram의 value가 0이 아니라면 개수가 다른 것이므로
    if i != 0:
        print("NO")
        break
else:
    print("YES")
