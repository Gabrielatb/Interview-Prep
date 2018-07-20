class Queue(object):
    """Simple FIFO queue, implemented using a list.

    This is a non-optimal way to make a queue--but it's just here as a demo
    of using a queue. Much better would be to use a linked list or
    collections.deque.
    """

    def __init__(self):
        self._data = []

    def enqueue(self, node):
        """Add item to end of queue."""

        self._data.append(node)

    def dequeue(self):
        """Remove item from start of queue and return."""

        return self._data.pop(0)

    def is_empty(self):
        """Is the queue empty?"""

        return not self._data

    def peek(self):
        """Return (but don't pop!) first item from start."""

        return self._data[0]
