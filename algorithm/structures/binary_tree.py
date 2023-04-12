class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def size(self):
        size = 1
        if self.left:
            size += self.left.size()
        if self.right:
            size += self.right.size()
        return size

    def depth(self):
        l,r = 0,0
        if self.left:
            l = self.left.depth()+1
        if self.right:
            r = self.right.depth()+1
        return max(l,r)

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal

    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal

      
class binary_tree:
    def __init__(self, root=None):
        self.root = root

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def depth(self):
        if self.root:
            return self.root.depth()+1
        else:
            return 0

    def traversal(self, sel = 1):
        if self.root:
            if sel==1:
                return self.root.preorder()
            if sel==2:
                return self.root.inorder()
            if sel==3:
                return self.root.postorder()
        else:
            return []
'''
대충 이런 트리
            10
          /    \
        20      30
       /  \       \
     40    50      60
    /    /   \
  100  1000  2000
  / \
200 300

size = 11
depth = 5
 pre-order = [10, 20, 40, 100, 200, 300, 50, 1000, 2000, 30, 60]
  in-order = [200, 100, 300, 40, 20, 1000, 50, 2000, 10, 30, 60]
post-order = [200, 300, 100, 40, 1000, 2000, 50, 20, 60, 30, 10]
'''
if __name__ == "__main__":
    r = Node(10)
    r.left = Node(20)
    r.right = Node(30)
    r.left.left = Node(40)
    r.left.right = Node(50)
    r.right.right = Node(60)
    t = Node(100)
    t.left = Node(200)
    t.right = Node(300)
    r.left.left.left = t
    r.left.right.left = Node(1000)
    r.left.right.right = Node(2000)
    tr = binary_tree(r)
    print(tr.size())
    print(tr.depth())
    print(tr.traversal(1))
    print(tr.traversal(2))
    print(tr.traversal(3))
