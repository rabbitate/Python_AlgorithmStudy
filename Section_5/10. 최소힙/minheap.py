# 최소힙 구현
 
import sys

# heap에 n을 삽입하는 함수
def heap_insert():
    h.append(n) # heap의 마지막에 삽입
    last_index = len(h)-1 # 삽입한 마지막 값의 index

    # 크기에 맞는 자리를 찾아준다
    while last_index > 1:
        parent_index = last_index//2 # 부모 노드의 index
        # 부모 노드의 값이 더 크다면
        if h[last_index] < h[parent_index]:
            h[last_index], h[parent_index] = h[parent_index], h[last_index] # swap 
            last_index = parent_index # 비교를 위해 부모 노드의 index를 기준으로 설정
        else: break

# 루트 노드 안에 있는 값을 삭제하고 반환해주는 함수(삭제할 값이 없다면 -1 반환)
def heap_delete():
    if len(h) == 1: return -1 # heap에 값이 없다면 -1 반환
    rdata = h[1] # return data를 루트 노드 값으로 초기화
    h[1] = h[-1] # 루트 노드를 heap의 마지막 값으로 초기화
    h.pop() # 마지막 값(노드) 삭제
    index = 1 # 비교를 위한 기준 노드 index

    # 크기에 맞는 자리를 찾아준다
    while True:
        left_index = index*2 # 왼쪽 자식 노드 index
        right_index = index*2 + 1 # 오른쪽 자식 노드 index

        # 자식 노드가 없는 경우
        if (len(h)-1) < left_index:
            break
        # 왼쪽 자식 노드만 있는 경우
        elif (len(h)-1) == left_index:
            # 왼쪽 자식 노드 값이 더 작을 경우
            if h[index] > h[left_index]:
                h[index], h[left_index] = h[left_index], h[index] # swap
                index = left_index # 왼쪽 자식 노드를 기준 노드로 설정
            else: break
        # 자식 노드가 두 개 있는 경우
        else:
            # 오른쪽 자식 노드 값보다 왼쪽 자식 노드 값이 더 작다면
            if h[left_index] < h[right_index]:
                # 기준 노드 값보다 왼쪽 자식 노드 값이 더 작을 때
                if h[index] > h[left_index]:
                    h[index], h[left_index] = h[left_index], h[index] # swap
                    index = left_index # 왼쪽 자식 노드를 기준 노드로 설정
                else: break
            # 왼쪽 자식 노드 값보다 오른쪽 자식 노드 값이 같거나 작다면
            else:
                # 기준 노드 값보다 오른쪽 자식 노드 값이 더 작을 때
                if h[index] > h[right_index]:
                    h[index], h[right_index] = h[right_index], h[index] # swap
                    index = right_index # 오른쪽 자식 노드를 기준 노드로 설정
                else: break

    return rdata # return data 반환

# sys.stdin = open("in3.txt", 'r')

h = [-1] # 계산의 편의를 위해 index는 1부터

while True:
    n = int(input())
    if n == -1:
        break
    elif n == 0:
        print(heap_delete())
    else:
        heap_insert()
