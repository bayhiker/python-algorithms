class FreqStack:
    """
    Use a PriorityQueue, and push in a tuple (-freq, -sn, num), where
    - sn is assigned from a global var starting from 0 and in creases with every push
    - negate freq and sn because Python PriorityQueue is a min-priority-queue
    - a global freq: dict[int, int], num->freq of num, updated with push and pop

    Note about python PriorityQueue, if you provide a tuple (-freq, -sn, num), it
    will automatically compare them with all three elements of the tuple, with the ones
    on the left having more weight.
    """

    def __init__(self):
        pass

    def push(self, val: int) -> None:
        pass

    def pop(self) -> int:
        pass


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
