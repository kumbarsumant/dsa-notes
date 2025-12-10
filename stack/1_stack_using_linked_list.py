class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

    def __str__(self):
        return self.value


class Stack:
    def __init__(self):
        self._length = 0
        self._head = None

    def push(self, value):
        node = Node(value)

        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node

        self._length += 1

    def pop(self):
        if self._head is None:
            raise RuntimeError("Cannot pop elements from the empty stack")

        value = self._head.value
        self._head = self._head.next
        self._length -= 1
        return value

    def top(self):
        if self._head is None:
            raise RuntimeError("Cannot access top element of the empty stack")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def _get_stack_elements(self):
        elements = [0] * self._length
        current_node = self._head
        i = self._length - 1

        while i >= 0:
            element = current_node.value
            elements[i] = element
            current_node = current_node.next
            i -= 1
        return elements

    def __len__(self):
        return self._length

    def __str__(self):
        elements = self._get_stack_elements()
        return str(elements)


if __name__ == "__main__":
    s = Stack()
    print("stack:", s)

    for i in range(5):
        element = i + 1
        s.push(element)
        print(f"pushed element {element}. stack: {s}. length: {len(s)}")

    print()
    print("is stack empty:", s.is_empty())
    print("current length of stack:", len(s))
    print("current top element of stack: ", s.top())
    print()

    for i in range(5):
        element = s.pop()
        print(f"popped element {element}. stack: {s}. length: {len(s)}")

    print()
    print("is stack empty:", s.is_empty())
    print("current length of stack:", len(s))

    try:
        s.pop()
    except Exception as error:
        print("error occurred while popping:", error)

    try:
        s.top()
    except Exception as error:
        print("error occurred while getting top element:", error)
