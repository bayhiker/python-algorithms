class Solution(object):
    def rearrangeString(self, s, k):
        return self.rearrange_string(s, k)

    def rearrange_string(self, s, k):
        from queue import Queue, PriorityQueue

        q: Queue[(int, str)] = Queue()  # (Remaining occurrences, char)
        pq: PriorityQueue[(int, str)] = PriorityQueue()  # (remaining occurrences, char)
        freq: dict[str:int] = {}  # char -> overall occurrences

        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        for c in freq:
            pq.put((-freq[c], c))

        rearranged: list[str] = []
        while not pq.empty():
            (negative_occurrences_left, c) = pq.get()
            rearranged.append(c)
            q.put((-negative_occurrences_left - 1, c))
            if q.qsize() >= k:
                (occurrences_left, c) = q.get()
                if occurrences_left > 0:
                    pq.put((-occurrences_left, c))
        leftover_chars = False
        while q.qsize() > 0:
            (occurrences_left, c) = q.get()
            if occurrences_left > 0:
                return ""
        return "".join(rearranged)
