class Node:
    def __init__(self):
        self.next = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = Node()


    def find(self, s: str) -> Node:
        node = self.root
        for char in s:
            if not char in node.next:
                raise Exception(node, char)
            node = node.next[char]
        return node
    

    def insert(self, word: str) -> None:
        while True:
            try:
                self.find(word).isEnd = True
                return
            except Exception as error:
                node, char = error.args
                node.next[char] = Node()

        
    def search(self, word: str) -> bool:
        try:
            return self.find(word).isEnd
        except:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        try:
            self.find(prefix)
            return True
        except:
            return False