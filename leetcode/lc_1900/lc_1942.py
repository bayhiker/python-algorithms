class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        return self.smallest_chair(times, targetFriend)

    def smallest_chair(self, times: list[list[int]], target_friend: int) -> int:
        # Use max_chair_no = 0 to track max number of chairs ever allocated
        # Use PriorityQueue pq_chairs to store available chairs before max_chair_no,
        # Use pq_leaving: PriorityQueue(leaving_time, chair_no) to track leaving time
        #
        # Sort all events by start time.
        #
        # Every time a new friend arrives, first pop all pq_leaving roots and enqueue those chairs
        # into pq_chair until leaving_time is greater than the new arrival time,
        # then grab min chair from pq_chair and assign it to this new arrival, if pq is empty
        # assign max_chair_no to this friend and max_chair_no +=1,
        # If this new arrivall is targetFriend, then return chair_no, otherwise,
        # then put (leaving_time, chair_no) into pq_leaving.
        #
        pass
