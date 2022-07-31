# 후위 표기식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.

import sys

sys.stdin = open("in5.txt", 'r')

postfix = list(input())
stack = [] # 후위 표기식 계산을 위한 stack

for i in postfix:
    # 숫자라면 stack에 push
    if i.isdecimal():
        stack.append(int(i))
    # 연산자라면
    else: 
        # 후위 표기식과 중위 표기식의 숫자의 순서는 같기 때문에
        b = stack.pop() 
        a = stack.pop() # 두 번째로 pop된 수가 a여야 한다

        # 연산자에 따라 계산하고 계산한 값을 다시 push해준다
        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        elif i == '/':
            stack.append(a/b)

print(stack.pop())
