from collections import Counter
from itertools import accumulate
from functools import lru_cache


class Solution:
    def maxHappyGroups(self, batchSize: int, groups: list[int]) -> int:
        return self.max_happy_groups_greedy_permutations(batchSize, groups)

    def max_happy_groups_greedy_permutations(
        self, batch_size: int, groups: list[int]
    ) -> int:
        max_groups_perm = 0

        @lru_cache(None)
        def permute(prefix: tuple[int], leftover_groups: tuple[int]) -> None:
            nonlocal max_groups_perm
            if not leftover_groups:
                # prefix is a permutation
                curr_sum = 0
                happy_groups = 0
                for g in prefix:
                    curr_sum = (curr_sum + g) % batch_size
                    if curr_sum == 0:
                        happy_groups += 1
                if curr_sum != 0:
                    # Left over groups, 1 of them can be happy by following the last paired group
                    happy_groups += 1
                if happy_groups > max_groups_perm:
                    max_groups_perm = happy_groups
                    print(f"max set to {max_groups_perm} with {prefix}")
            else:
                for i in range(len(leftover_groups)):
                    new_leftover_groups = leftover_groups[1:]
                    new_prefix = list(prefix[0:]) + [leftover_groups[i]]
                    permute(tuple(new_prefix), tuple(new_leftover_groups))

        n = len(groups)
        groups = [groups[i] % batch_size for i in range(n) if groups[i] % batch_size]
        counter = Counter(groups)
        # Groups divisible by batch_size are fed first and are always happy
        total = n - len(groups)
        for i in range(1, (batch_size + 1) // 2):
            comp_group_size = batch_size - i
            if i in counter and comp_group_size in counter:
                pairs = (
                    min(counter[i], counter[comp_group_size])
                    if i != comp_group_size
                    else counter[i] // 2
                )
                total += pairs
                counter[i] -= pairs
                counter[comp_group_size] -= pairs
        # For leftover groups that cannot be paired up, use memoized brute-force
        leftover_groups = []
        for i in counter:
            leftover_groups += [i] * counter[i]
        permute((), tuple(leftover_groups))
        print(f"total is {total} max_groups_perm is {max_groups_perm}")
        return total + max_groups_perm

        return total

    # TODO Check why test case is returning 17
    # 7, [2,7,5,2,3,2,6,5,3,6,2,3,7,2,2,5,4,6,6,4,7,5,6,1,6,2,6,6,2,5]
    def max_happy_groups_greedy_counting(
        self, batch_size: int, groups: list[int]
    ) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def find_the_rest(remainder: int, leftover_groups: tuple[int]) -> int:
            if not leftover_groups:
                return 0
            total_rest = 0
            for i in range(len(leftover_groups)):
                new_leftover_groups = leftover_groups[:i] + leftover_groups[i + 1 :]
                new_remainder = (remainder + groups[i]) % batch_size
                total_rest = max(
                    total_rest,
                    (remainder == 0)
                    + find_the_rest(new_remainder, tuple(new_leftover_groups)),
                )
                print(f"{leftover_groups[i]}:{total_rest},", end="")
            print(
                f"\ntotal_rest {total_rest}, remainder {remainder}, leftover {leftover_groups}"
            )
            return total_rest

        n = len(groups)
        groups = [groups[i] % batch_size for i in range(n) if groups[i] % batch_size]
        counter = Counter(groups)
        # Groups divisible by batch_size are fed first and are always happy
        total = n - len(groups)
        for i in range(1, (batch_size + 1) // 2):
            comp_group_size = batch_size - i
            if i in counter and comp_group_size in counter:
                pairs = (
                    min(counter[i], counter[comp_group_size])
                    if i != comp_group_size
                    else counter[i] // 2
                )
                total += pairs
                counter[i] -= pairs
                counter[comp_group_size] -= pairs
        # For leftover groups that cannot be paired up, use memoized brute-force
        leftover_groups = []
        for i in counter:
            leftover_groups += [i] * counter[i]
        total += find_the_rest(0, tuple(leftover_groups))

        return total

    def max_happy_groups_greedy_recursive(
        self, batch_size: int, groups: list[int]
    ) -> int:
        # Only group_size % batch_size matters
        groups = [g % batch_size for g in groups]
        groups.sort(reverse=True)
        total = 0
        while len(groups) > 0 and groups[-1] == 0:
            total += 1
            print(f"Found 0")
            groups.pop()

        factor = 1
        while True:
            if sum(groups) < batch_size * factor:
                break
            unserved_groups = []  # groups that has yet to be scheduled
            while len(groups) > 0:
                g = groups[0]
                supplemental_groups = self.get_groups(
                    groups[1 : len(groups)], batch_size * factor - g
                )
                if not supplemental_groups:
                    unserved_groups.append(g)
                else:
                    total += 1
                    print(f"Found {g} {supplemental_groups}")
                    for x in supplemental_groups:
                        groups.remove(x)
                groups.remove(g)
            groups = unserved_groups
            factor += 1

        return total + 1 if groups else total

    from functools import lru_cache

    @lru_cache
    def get_groups(self, groups: list[int], expected_sum: int) -> list[int]:
        if len(groups) == 0:
            return []
        sum_all = sum(groups)
        if sum_all <= expected_sum:
            return groups if sum_all == expected_sum else []
        for g in groups:
            if g == expected_sum:
                return [g]
            elif g > expected_sum:
                continue
            new_groups = groups.copy()
            new_groups.remove(g)
            supplemental_groups = self.get_groups(new_groups, expected_sum - g)
            if supplemental_groups:
                supplemental_groups.append(g)
                return supplemental_groups
            else:
                return []
