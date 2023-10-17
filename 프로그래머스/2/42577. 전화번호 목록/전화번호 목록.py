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
            if node.isEnd:
                return False
            if not char in node.next:
                node.next[char] = Node()
            node = node.next[char]
        node.isEnd = True
        if node.next:
            return False
        
        return True
        
    
def find(node) -> bool:
    if node.isEnd and node.next:
        return False
    if node.isEnd and not node.next:
        return True
    return all(find(n) for n in node.next.values())


def solution(phone_book):
    t = Trie()
    return all(t.insert(p) for p in phone_book)
        