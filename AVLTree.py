import copy


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(root):
    if root == None:
        return 0
    return root.height


def isbalanced(root):
    if root == None:
        return 0
    return height(root.left) - height(root.right)


def rotateRight(root):
    # if root == None:
    # 	return None
    # print(root)
    x = root.left
    # print(x)
    T2 = x.right
    x.right = root
    root.left = T2

    root.height = max(height(root.left), height(root.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x


def rotateLeft(root):
    # if root == None:
    # 	return None
    x = root.right
    T2 = x.left
    x.left = root
    root.right = T2

    root.height = max(height(root.left), height(root.right)) + 1
    x.height = max(height(x.left), height(x.right)) + 1
    return x


def insertAVL(root, key):
    if root == None:
        return Node(key)

    if key < root.key:
        root.left = insertAVL(root.left, key)
    elif key > root.key:
        root.right = insertAVL(root.right, key)
    else:
        return root
    root.height = 1 + max(height(root.left), height(root.right))

    balance = isbalanced(root)
    if balance > 1 and key < root.left.key:
        root = rotateRight(root)
    elif balance > 1 and key > root.left.key:
        root.left = rotateLeft(root.left)
        root = rotateRight(root)
    elif balance < -1 and key > root.right.key:
        root = rotateLeft(root)
    elif balance < -1 and key < root.right.key:
        root.right = rotateRight(root.right)
        root = rotateLeft(root)
    return root


def preOrder(root):
    if root == None:
        return
    preOrder(root.left)
    print(root.key)
    preOrder(root.right)


root = Node(2)
root = insertAVL(root, 10)
root = insertAVL(root, 20)
root = insertAVL(root, 30)
root = insertAVL(root, 40)
root = insertAVL(root, 50)
root = insertAVL(root, 25)
print(preOrder(root))
