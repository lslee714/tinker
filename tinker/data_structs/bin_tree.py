


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None or val == self.val:
            self.val = val
        else:
            if val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
            else:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)

    def search(self, val):
        if val == self.val:
            return True
        elif val > self.val and self.right:
            return self.right.search(val)
        elif val < self.val and self.left:
            return self.left.search(val)
        else:
            return False

    def __contains__(self, val):
        return self.search(val)
