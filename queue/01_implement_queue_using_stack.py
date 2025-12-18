"""
PROBLEM: Implement Queue using Stacks
------------------------------------
Implement a first-in-first-out (FIFO) queue using only two stacks.
The implemented queue should support: enqueue, dequeue, front, and len.

Note: You must use only standard stack operations (append and pop in Python).
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
- A Stack is LIFO (Last-In, First-Out). If you push [1, 2, 3], the '3' sits on
   top, trapping the '1' at the bottom. A Queue needs that '1' first.

- By using two stacks, we can reverse the order.
  - s1 (Inbox): Always receives new elements.
  - s2 (Outbox): When dequeue/front request comes transfer s1 elements to s2. Now the
    order will be reversed in s2. We can remove the elements from stack s2.

- We only transfer from s1 to s2 when s2 is empty. This way, each element is
  pushed and popped a constant number of times, keeping operations
  efficient (Amortized O(1)) despite the occasional loop.
"""


class Queue:
    def __init__(self):
        self.s1 = []  # Inbox
        self.s2 = []  # Outbox

    def enqueue(self, value):
        self.s1.append(value)

    def _transfer_s1_to_s2(self):
        while self.s1:
            self.s2.append(self.s1.pop())

    def dequeue(self):
        if not self.s1 and not self.s2:
            raise RuntimeError("Cannot dequeue from empty queue")
        if not self.s2:
            self._transfer_s1_to_s2()
        return self.s2.pop()

    def front(self):
        if not self.s1 and not self.s2:
            raise RuntimeError("Cannot fetch first element from empty queue")
        if not self.s2:
            self._transfer_s1_to_s2()
        return self.s2[-1]

    def __len__(self):
        return len(self.s1) + len(self.s2)


if __name__ == "__main__":
    q = Queue()

    # Test sequence
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(f"Initial Front: {q.front()}")  # Expected: 1
    print(f"Dequeued: {q.dequeue()}")  # Expected: 1

    q.enqueue(4)
    print(f"New Front: {q.front()}")  # Expected: 2
    print(f"Current Length: {len(q)}")  # Expected: 3 (elements: 2, 3, 4)

    while len(q) > 0:
        print(f"Emptying Queue: {q.dequeue()}")
