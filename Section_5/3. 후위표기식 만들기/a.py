# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
# 중위표기식은 우리가 흔히 쓰은 표현식입니다. 즉 3+5 와 같이 연산자가 피연산자 사이에 있 으면 중위표기식 입니다.
# 후위표기식은 35+ 와 같이 연산자가 피연산자 뒤에 있는 표기식 입니다.
# 예를 들어 중위표기식이 3+5*2 를 후위표기식으로 표현하면 352*+ 로 표현됩니다.
# 만약 다음과 같이 연산 최우선인 괄호가 표현된 식이라면
# (3+5)*2 이면 35+2*로 바꾸어야 합니다.

import sys

sys.stdin = open("in2.txt", 'r')

infix = list(input()) # 중위 표기식을 입력받는다

postfix = [] # 후위 표기식 리스트
operator = [] # 연산자 스택, 우선순위가 높은 순으로 pop시킬 수 있도록 스택 사용

for i in infix:
    # i가 숫자라면
    if i.isdecimal():
        postfix.append(i) # 후위 표기식에 push
    # i가 연산자나 괄호라면
    else:
        if i == '(':
            operator.append(i) # '(' push
        elif i == '*' or i == '/':
            # i가 '*'나 '/'일 경우, 먼저 push된 '*'나 '/'를 제외하곤 우선순위가 높으므로
            while operator and (operator[-1] == '*' or operator[-1] == '/'):
                postfix.append(operator.pop())
            operator.append(i) # i push
        elif i == '+' or i == '-':
            # i가 '+'나 '-'일 경우, 스택에 있는 모든 연산자보다 우선순위가 낮으므로
            while operator and operator[-1] != '(':
                postfix.append(operator.pop()) 
            operator.append(i) # i push
        # 괄호가 닫혔다면
        elif i == ')':
            while operator[-1] != '(':
                postfix.append(operator.pop())
            operator.pop() # '(' pop

# 연산자 스택에 남아있는 연산자들을 우선순위 순으로 pop
while operator:
    postfix.append(operator.pop())

for i in postfix:
    print(i,end="")
