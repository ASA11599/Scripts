class Trie(object):

    def __init__(self):
        self.root = {}

    def add(self, word):
        current = self.root
        for c in word:
            if not (c in current):
                current[c] = {}
            current = current[c]

    def contains(self, word):
        current = self.root
        for c in word:
            if not (c in current):
                return False
            else:
                current = current[c]
        return True


if __name__ == "__main__":
    t = Trie()
    t.add("abcd")
    t.add("bcda")
    print(t.contains("a"))
    print(t.contains("b"))
    print(t.contains("abcde"))
