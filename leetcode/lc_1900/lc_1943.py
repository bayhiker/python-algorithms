from collections import defaultdict


class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        return self.split_painting_prefix_sum(segments)

    def split_painting_prefix_sum(self, segments: list[list[int]]) -> list[list[int]]:
        color_actions = defaultdict(int)
        for l, r, c in segments:
            color_actions[l] += c
            color_actions[r] -= c
        s = sorted([p, color_actions[p]] for p in color_actions)
        mixed_colors: list[list[int]] = []
        for i in range(len(s) - 1):
            s[i + 1][1] += s[i][1]
            if s[i][1] > 0:
                mixed_colors.append([s[i][0], s[i + 1][0], s[i][1]])
        return mixed_colors

    def split_painting_endpoints(self, segments: list[list[int]]) -> list[list[int]]:
        m = len(segments)
        s: set[int] = set()
        for segment in segments:
            s.add(segment[0])
            s.add(segment[1])
        endpoints = list(s)
        n = len(endpoints)
        # All possible start or stop points
        endpoints.sort()
        # mixed colors[i] is mixed colors for segment [endpoints[i], endpoints[i+1])
        mixed_colors = [[] for i in range(n - 1)]
        segments.sort(key=lambda s: s[0])
        start_index = 0
        for i in range(m):
            segment = segments[i]
            while segment[0] > endpoints[start_index]:
                start_index += 1
            j = start_index
            while endpoints[j] < segment[1]:
                mixed_colors[j].append(segment[2])
                j += 1
        description = []
        for i in range(len(mixed_colors)):
            if mixed_colors[i]:
                description.append(
                    [endpoints[i], endpoints[i + 1], sum(mixed_colors[i])]
                )
        return description
