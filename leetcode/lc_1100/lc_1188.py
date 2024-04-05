""" Design bounded blocking queue
Description

Implement a thread safe bounded blocking queue that has the following methods:

    BoundedBlockingQueue(int capacity) The constructor initializes the queue with a maximum capacity.
    void enqueue(int element) Adds an element to the front of the queue. If the queue is full,
            the calling thread is blocked until the queue is no longer full.
    int dequeue() Returns the element at the rear of the queue and removes it. If the queue is empty,
            the calling thread is blocked until the queue is no longer empty.
    int size() Returns the number of elements currently in the queue.

Your implementation will be tested using multiple threads at the same time.
Each thread will either be a producer thread that only makes calls to the enqueue method or
a consumer thread that only makes calls to the dequeue method.
The size method will be called after every test case.

Please do not use built-in implementations of bounded blocking queue as this will
not be accepted in an interview.
"""
"""
Solution: Use threading.Semaphore and optionally a Lock if queue object in the language is
note thread safe already. Python Queue is already thread safe making get and offer don't mess
with on another, so no Lock needed for Python implementation.
"""
# Sample implementation from
# https://github.com/MyCuteGuineaPig/Leetcode/blob/master/Concurrency/1188.%20Design%20Bounded%20Blocking%20Queue.py
import threading
import collections


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.cv = threading.Condition()
        self.q = collections.deque()
        self.capa = capacity
        self.count = 0

    def enqueue(self, element: int) -> None:
        with self.cv:
            while self.count == self.capa:
                self.cv.wait()
            self.q.append(element)
            self.count += 1
            self.cv.notify()

    def dequeue(self) -> int:
        val = 0
        with self.cv:
            while self.count == 0:
                self.cv.wait()
            val = self.q.popleft()
            self.count -= 1
            self.cv.notify()
        return val

    def size(self) -> int:
        with self.cv:
            return len(self.q)
