class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        return self.group_strings_dfs(words)

    def group_strings_dfs(self, words: list[str]) -> list[int]:
        # Since each string has at most 26 letters, each letter appearing at most once
        # Use a bit-mask to represent each string, 2 strings are connected if there are
        # only 0 or 1 or 2 bits flipped: 0 replace with self, 1 bit remove or add, 2 bit replace with diff letter
        # Now use DFS from a str to search for all neighbors, keep going until all strings are visited
        pass

    def group_strings_union_find(self, words: list[str]) -> list[int]:
        # Union-find, union two groups if one member from each group are connected,
        # repeat until the groups cannot be merged any more.
        # Use an array to indicate group membership of strings, group membership
        # can be indicated by, for example, the smallest index of the strings in that group
        pass
