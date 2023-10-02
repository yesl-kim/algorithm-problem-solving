class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.next:
                node.next[char] = Node(char)
            node = node.next[char]
        node.word = word

        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not char in node.next:
                return False
            node = node.next[char]
        return node.word == word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not char in node.next:
                return False
            node = node.next[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)