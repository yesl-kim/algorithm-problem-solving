class Node:
    def __init__(self):
        self.next = {}
        self.word: str = None # 최종 단어, 데이터 존재여부 = 마지막 노드여부
        self.checked = False # res 포함여부, 중복처리를 위함

class Solution:
    def __init__(self):
        self.root = Node()
        
    def create_trie(self, words):
        for word in words:
            self.insert(word)
            
    def insert(self, word):
        node = self.root
        for char in word:
            if not char in node.next:
                node.next[char] = Node()
            node = node.next[char]
        node.word = word
            
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.create_trie(words)
        
        
        
        res = []
        h, w = len(board), len(board[0])
        def find(x, y, node):
            if not node:
                return
            if node.word and not node.checked:
                res.append(node.word)
                node.checked = True
            for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
                xx, yy = x+dx, y+dy
                if 0<=xx<h and 0<=yy<w and board[xx][yy] != '_' and board[xx][yy] in node.next:
                    char = board[xx][yy]
                    board[xx][yy] = '_'
                    find(xx, yy, node.next[char])
                    board[xx][yy] = char
                
        for i in range(h):
            for j in range(w):
                char = board[i][j]
                if char in self.root.next:
                    board[i][j] = '_'
                    find(i, j, self.root.next[char])
                    board[i][j] = char
                    
        return res