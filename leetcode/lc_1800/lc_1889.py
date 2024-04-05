from bisect import bisect_right


class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        return self.min_wasted_space(packages, boxes)

    def min_wasted_space(self, packages: list[int], boxes: list[list[int]]) -> int:
        # Sort and use partial sum of packages to calculate waste space
        # Sort boxes[i], boxes[i][j] will be used for all package[x] smaller than or equal to it
        m = len(packages)
        packages.sort()
        sum_packages = [packages[0]] * m
        for i in range(1, m):
            sum_packages[i] = sum_packages[i - 1] + packages[i]

        min_waste_space = 10**10  # Based on constraints
        for supplier in boxes:
            waste, next_package = 0, 0  # processed is last packaged processed
            supplier.sort()
            for box in supplier:
                new_next_package = bisect_right(packages, box, lo=next_package, hi=m)
                if new_next_package <= next_package:  # Not a usable box
                    continue
                used = sum_packages[new_next_package - 1] - (
                    sum_packages[next_package - 1] if next_package > 0 else 0
                )
                waste += box * (new_next_package - next_package) - used
                next_package = new_next_package
                if next_package == m:
                    break
            if next_package == m:
                # Otherwise there are leftover packages, not a valid supplier
                min_waste_space = min(min_waste_space, waste)

        return -1 if min_waste_space == 10**10 else min_waste_space % (10**9 + 7)
