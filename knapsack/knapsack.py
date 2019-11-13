#!/usr/bin/python

import sys
from math import floor
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])


class MaxHeap(list):
    """MaxHeap keeps maximum element available for pop in O(log n) time.
    Inherits from list.
    Overrides methods pop, insert and clear.

    Instantiate a new, empty MaxHeap:
    >>>max_heap = MaxHeap()
    Heapify an array of: int, float, str or tuple; Q:
    >>>max_heap.max_heapify([2, 4, 7, 1, 3])
    Insert a new value into heap:
    >>>max_heap.insert(5)
    Pop maximum value from heap:
    >>>max_heap.pop()
    1
    Peek maximum value in heap:
    >>>max_heap.peek()
    2
    Clear heap of all data:
    >>>clear()
    Check heap is empty:
    >>>is_empty()
    True
    """

    def __init__(self) -> None:
        """MaxHeap instantiated as an empty list with size 0."""
        self.size = 0
        super(MaxHeap, self).__init__()

    def is_empty(self) -> int:
        """Returns True if heap is empty.
        :return: bool
        """
        return self.size == 0

    def max_heapify(self, array: list) -> list:
        """Heapifies a given array.
        Sets self as array.
        Calls _sift_down for each index capable of having a child the last of which we call last_parent.
        :param array: Array to heapify.
        :return: Heapified array.
        """
        if not isinstance(array, list):
                raise TypeError(f'max_heapify accepts type: list. You have entered type: {type(array)}')
        else:
            self.clear()
            self += array
            self.size = len(self)

        # We only need to call _sift_down from the last parent to the start of the list as
        # higher indexes have children with indexes higher than len(array).
        last_parent = floor((self.size - 1) / 2)
        for i in range(last_parent, -1, -1):
            self._sift_down(i)
        return self

    def pop(self, **kwargs):
        """Removes and returns maximum value from MaxHeap or notification of empty heap.
        Swaps maximum at root with value at end of list, pops max value from end of list and
        sifts new root down to correct position.
        :return: int, float, str, or tuple.
        """
        # Move min value to the end of list for easy popping, move last value to root.
        if self:
            self[0], self[-1] = self[-1], self[0]
            popped = super(MaxHeap, self).pop()
            self.size -= 1

            # Sift the new root value down.
            self._sift_down(0)
            return popped
        else:
            return 'MaxHeap is empty.'

    def peek(self):
        """Returns maximum value or notification of empty heap.
        :return: int, float, str or tuple.
        """
        if self:
            return self[0]
        else:
            return 'MaxHeap is empty.'

    def insert(self, data, **kwargs) -> None:
        """Appends data to heap, increments size, and calls _sift_up with last index in heap.
        :param data: int, float, str or tuple.
        """
        # if not isinstance(data, int or float or tuple or str):
        #     raise TypeError(f'insert accepts types: int, float, tuple, or str. You have entered {type(data)}')
        # else:
        super(MaxHeap, self).append(data)
        self.size += 1
        self._sift_up(self.size - 1)

    def _sift_up(self, i: int) -> None:
        """Swaps data at heap[i] with its parent if parent is smaller and calls _sift_up on parent index.
        :param i: An index of self
        """
        parent = floor((i - 1) / 2)
        if self[i][1] > self[parent][1]:
            self[i], self[parent] = self[parent], self[i]
        if parent > 0:
            self._sift_up(parent)

    def _sift_down(self, i: int) -> None:
        """Sifts data down heap.
        Finds left and right children of heap[i]
        Checks if either child is larger and swaps with the largest.
        Calls _sift_down on index of swap.
        :param i: An index of self
        """
        left = i * 2 + 1
        right = i * 2 + 2
        biggest = i

        # Check if children are within array. Find largest value among the three.
        if left < self.size and self[left][1] > self[biggest][1]:
            biggest = left
        if right < self.size and self[right][1] > self[biggest][1]:
            biggest = right
        if biggest != i:
            # If we found a child with a larger value, swap it with the parent.
            self[i], self[biggest] = self[biggest], self[i]
            if biggest * 2 < self.size:
                # If children of biggest are within array, sift it down further.
                self._sift_down(biggest)

    def max_merge(self, max_heap_1: list, max_heap_2: list) -> list:
        """Merges two lists into a MaxHeap.
        :param max_heap_1: A list
        :param max_heap_2: A list
        :return: A max_heap
        """
        new_max = max_heap_1 + max_heap_2
        return self.max_heapify(new_max)

    def clear(self) -> None:
        """Clears heap of all data."""
        self.size = 0
        super(MaxHeap, self).clear()


def knapsack_solver(items, capacity):
    """Solving the Knapsack problem using a max heap.

    Store each item with its value/size ratio as the key for the heap ensures the next
    best item to keep is always an O(1) grab from the heap.

    Keep popping from the heap and adding to the knapsack until no more items fit.

    This works for all but the largest test case. I need to find a way to swap an item on
    some condition I haven't worked out. Yet.

    Adding items to the heap is worst-case O(n log n) but average case O(1) so running
    through all items is O(n).
    Popping from the heap is O(log n). We do this n times.
    The total time complexity is O(n log n).
    """
    # Use a heap to keep the highest value/size items at the top.
    max_heap = MaxHeap()
    for item in items:
        # Make tuple with the item and its value/size ratio
        new = (item, item[2] / item[1])
        max_heap.insert(new)

    # Keep track of our current size and value. Store the items we're keeping.
    size, value, final = 0, 0, []

    # Look through all the items.
    while not max_heap.is_empty():
        next_item = max_heap.pop()
        # Check that this item will fit in our knapsack.
        if size + next_item[0][1] > capacity:
            # Something needs to go here to determine if a swap can/needs to happen.
            # Maybe final needs to be a heap sorted by ???
            # I can't figure out how it would work.
            continue

        # Store the item and increment our trackers.
        else:
            final.append(next_item)
            size += next_item[0][1]
            value += next_item[0][2]

    # Sort by item number and report value.
    return {'Chosen': sorted([x[0][0] for x in final]), 'Value': value}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        capacity = int(sys.argv[2])
        file_location = sys.argv[1].strip()
        file_contents = open(file_location, 'r')
        items = []

        for line in file_contents.readlines():
            data = line.rstrip().split()
            items.append(Item(int(data[0]), int(data[1]), int(data[2])))

        file_contents.close()
        print(knapsack_solver(items, capacity))
    else:
        print('Usage: knapsack.py [filename] [capacity]')