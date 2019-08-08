import collections
from typing import List


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(list)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for s in dict:
            self.map[len(s)].append(s)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for s in self.map[len(word)]:
            n = 0
            for a, b in zip(s, word):
                if a != b:
                    n += 1
            if n == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)

if __name__ == '__main__':
    obj = MagicDictionary()
    obj.buildDict(["hello", "leetcode"])
    print(obj.search("hello"))
    print(obj.search("hhllo"))
