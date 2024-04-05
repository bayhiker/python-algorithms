class Solution:
    def maximumRobots(
        self, chargeTimes: list[int], runningCosts: list[int], budget: int
    ) -> int:
        # Use two pointers start and end to track a floating window of robots.
        # Because all numbers are positive, expanding a window never decreases cost,
        # If less than budget, note windows size, then end+=1.
        # If mre than budge, start+=1
        # To calc total cost, use a sorted list or monotonic stack
        # to maintain largest item in window,
        # and use a window_sum to maintain sum(runningCost)
        #
        # Why can we use a monotonic stack to track max in window?
        # If a larger item joins the sliding window from the right,
        # we can safely pop off and throw away anything in the stack
        # that's smaller than it, because those will never be the max
        # later, they will be slid out of before this large item anyways
        pass
