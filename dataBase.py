class Node:
    def __init__(self, data):
        self.data = data

class Table:
    def __init__(self, columns):
        self.columns = columns

    def insertInto(self, data):
        node = Node(data)
        