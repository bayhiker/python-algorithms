class MagicDictionary:
    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: list[str]) -> None:
        self.words = dictionary

    def search(self, search_word: str) -> bool:
        for word in self.words:
            if len(search_word) != len(word):
                continue
            diff = 0
            for i in range(len(word)):
                if word[i] != search_word[i]:
                    diff += 1
            if diff == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
