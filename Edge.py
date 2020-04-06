class Edge:
    def __init__(self, tail, head):
        self.tail = tail
        self.head = head

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def reverse(self):
        temp = self.tail
        self.tail = self.head
        self.head = temp
