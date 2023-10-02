class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not char in node.next:
                node.next[char] = Node()
            node = node.next[char]
        node.isEnd = True

        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not char in node.next:
                return False
            node = node.next[char]
        return node.isEnd
        

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