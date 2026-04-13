class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1.
    def add_to_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 2.
    def add_to_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # 3.
    def remove_last(self):
        if not self.head:
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    # 4.
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 5.
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    # 6.
    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        for _ in range(position - 1):
            if not current:
                return
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # 7.
    def remove_by_value(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    # 8.
    def combine(self, other):
        if not self.head:
            self.head = other.head
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = other.head

    # 9.
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next  # сохраняем!
            current.next = prev       # переворачиваем
            prev = current
            current = next_node

        self.head = prev

    # 10.
    def sort(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next

            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next

                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head