
# key-value 데이터를 저장하는 이진탐색트리 구현.
'''
class binary_search_tree:
- insert(key,value)
- remove(key) -> boolean
- lookup(key) -> (target:node, parent:node)
- inorder()
- min() -> target:node
- max() -> target:node
'''

class Node:
    def __init__(self, key, data, left = None, right = None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def size(self):
        size = 1
        if self.left:
            size += self.left.size()
        if self.right:
            size += self.right.size()
        return size

    def insert(self, key, value):
        if self.key > key:
            if self.left:
                self.left.insert(key, value)
            else:
                self.left = Node(key, value)
        elif self.key < key:
            if self.right:
                self.right.insert(key, value)
            else:
                self.right = Node(key, value)
        else:
            raise KeyError("Key %s already exists."%key)

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def lookup(self, key, parent=None):
        if self.key > key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return (None, None)
        elif self.key < key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return (None, None)
        else:
            return (self, parent)

    def count_children(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self

    def max(self):
        if self.right:
            return self.right.max()
        else:
            return self

class binary_search_tree():
    def __init__(self, node = None):
        self.root = node

    def insert(self, key, value):
        if self.root:
            self.root.insert(key, value)
        else:
            self.root = Node(key, value)

    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            count = node.count_children()
            if count == 0:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    elif parent.right == node:
                        parent.right = None
                else:
                    self.root = None

            if count == 1:
                if node.left:
                    child = node.left
                elif node.right:
                    child = node.right
                if parent:
                    if parent.left == node:
                        parent.left = child
                    elif parent.right == node:
                        parent.right = child
                else:
                    self.root = child

            if count == 2:
                # l = node.left.size()
                # r = node.right.size()
                # 일단, 무조건 오른쪽.
                parent = node
                successor = node.right

                while successor.left:
                    parent = successor
                    successor = successor.left

                node.key = successor.key
                node.value = successor.value

                if parent.left == successor:
                    parent.left = successor.right
                elif parent.right == successor:
                    parent.right = successor.right

            return True # node (X)
        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    #원소 삭제를 위해 부모노드도 같이 리턴.
    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return (None, None)

    def min(self):
        if self.root:
            return self.root.min()
        else:
            return None

    def max(self):
        if self.root:
            return self.root.max()
        else:
            return None


import random
random.seed(144)
a = list(set(random.randint(10,99) for _ in range(20)))
print(a)
bst = binary_search_tree()
for i in a:
    bst.insert(i,0)
for i in bst.inorder():
    print(i.key,end=", ")
print()
bst.remove(20)
bst.remove(25)
bst.remove(94)
bst.remove(25)

for i in bst.inorder():
    print(i.key,end=", ")
print()
