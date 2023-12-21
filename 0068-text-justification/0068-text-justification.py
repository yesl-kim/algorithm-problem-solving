class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 총 길이 구하는 건,, 함수 분리 -> 그때그때 구하는게 좋을까
        padEnd = lambda s: s + ' ' * (maxWidth - len(s))
            
        def pack(words, width):
            words_num = len(words)
            if words_num == 1:
                return padEnd(words[0])
            
            share, rest = divmod(maxWidth - width, words_num - 1)
            space = ' ' * (share + 1)
            
            line = words[0]
            for i, word in enumerate(words[1:]):
                line += space + ' ' + word if i < rest else space + word
            return line
                
                
        line = [words[0]]
        width = len(words[0])
        output = []
        for word in words[1:]:
            new_width = width + len(word) + 1
            if new_width <= maxWidth:
                width = new_width
                line.append(word)
            else:
                output.append(pack(line, width))
                line = [word]
                width = len(word)
                
        if line:
            last_line = padEnd(" ".join(line))
            output.append(last_line)
            
        return output