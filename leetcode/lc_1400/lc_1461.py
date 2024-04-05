class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return self.has_all_codes(s, k)

    def has_all_codes(self, s: str, k: int) -> bool:
        found: list[bool] = [False] * 2**k
        for i in range(len(s) - k + 1):
            found[int(s[i : i + k], 2)] = True
        for i in found:
            if not i:
                return False
        return True

    def has_all_codes_count(self, s: str, k: int) -> bool:
        # Counting instead of checking all 2**k items
        count = 0
        found: list[bool] = [False] * 2**k
        for i in range(len(s) - k + 1):
            value = int(s[i : i + k], 2)
            if not found[value]:
                count += 1
                found[int(s[i : i + k], 2)] = True
        return count == 2**k
