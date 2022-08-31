# 이진 트리 순회

# 전위 순회
def Preorder(n):
    if len(tree)-1 >= n:
        print(tree[n], end=" ")
        Preorder(n*2)
        Preorder(n*2+1)

# 중위 순회
def Inorder(n):
    if len(tree)-1 >= n:
        Inorder(n*2)
        print(tree[n], end=" ")
        Inorder(n*2+1)

# 후위 순회
def Postorder(n):
    if len(tree)-1 >= n:
        Postorder(n*2)
        Postorder(n*2+1)
        print(tree[n], end=" ")

tree = list(map(int, input().split())) # 이진 트리
tree.insert(0,-1) # 계산 편의를 위해 삽입

print("전위 순회: ", end="")
Preorder(1)
print("\n중위 순회: ", end="")
Inorder(1)
print("\n후위 순회: ", end="")
Postorder(1)
