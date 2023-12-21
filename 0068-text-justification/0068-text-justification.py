class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        padEnd = lambda s: s + ' ' * (maxWidth - len(s))
        get_width = lambda words: len(words) - 1 + sum(len(w) for w in words)
            
        def pack(words):
            words_num = len(words)
            if words_num == 1:
                return padEnd(words[0])
            
            share, rest = divmod(maxWidth - get_width(words), words_num - 1)
            default_space = ' ' * (share + 1)
            line = words[0]
            for i, word in enumerate(words[1:]):
                space = default_space + ' ' if i < rest else default_space
                line += space + word
            return line
                
                
        line = [words[0]]
        output = []
        for word in words[1:]:
            width = get_width(line) + len(word) + 1
            if width <= maxWidth:
                line.append(word)
            else:
                output.append(pack(line))
                line = [word]
                
        if line:
            last_line = padEnd(" ".join(line))
            output.append(last_line)
            
        return output