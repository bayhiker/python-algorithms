class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        return self.max_num_of_substrings(s)

    def max_num_of_substrings(self, s: str) -> list[str]:
        # Step 1: scan s, use a hash to track first and last occurrence of a char
        # Step 2: scan s: expand start/end of c1 with c2 start/end if c2 falls between two c1's
        # Step 3: scan d: remove duplicate substring
        # Step 4: scan d: use greedy algorithm to pick the max num of
        #         substrings that have the shortest total length.
        #         Check next char, if its last char comes earlier than end of last item in result
        #         then pop the last in result and push in the current substr
        #
        d: dict[str : list[int]] = {}  # Elements of dict: [start, end]
        for i, c in enumerate(s):
            if not c in d:
                d[c] = [i, i]
            else:
                d[c][1] = i

        for i, c1 in enumerate(s):
            for c2 in d:
                if c1 != c2 and d[c2][0] < i and d[c2][1] > i:
                    # c1 falls into two c2 chars, expand c2 [start, end] to include all c1s
                    d[c2] = [min(d[c1][0], d[c2][0]), max(d[c1][1], d[c2][1])]

        # Remove duplicates: chars with the same start/end
        deduped_chars = list(d.keys())
        for c1 in d:
            for c2 in d:
                if c1 < c2 and c2 in deduped_chars and d[c1] == d[c2]:
                    deduped_chars.remove(c2)

        result: list[str] = []
        for i, c in enumerate(s):
            if not c in deduped_chars:  # Already processed, or duplicate
                continue
            deduped_chars.remove(c)
            curr_substring = s[d[c][0] : d[c][1] + 1]
            if not result:
                result.append(curr_substring)
                continue
            last_char = result[-1][0]
            if d[last_char][1] >= d[c][1]:
                result.pop()
                result.append(curr_substring)
            elif d[last_char][1] < d[c][0]:
                result.append(curr_substring)

        return result
