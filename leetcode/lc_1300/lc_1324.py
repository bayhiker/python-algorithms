class Solution:
    def printVertically(self, s: str) -> list[str]:
        return self.print_vertically(s)

    def print_vertically(self, s: str) -> list[str]:
        words = [0] + [len(w) for w in s.split(" ")]  # Word lengths
        max_word = max(words)
        for i in range(1, len(words)):
            words[i] = words[i - 1] + words[i] + 1
        # Now words[i] contain starting index of word[i], words[i+1] - 2 is the last char of word[i]
        result = []
        for i in range(max_word):
            vertical = ""
            for j in range(len(words) - 1):
                vertical += s[words[j] + i] if words[j] + i <= words[j + 1] - 2 else " "
            result.append(vertical.rstrip())
        return result
