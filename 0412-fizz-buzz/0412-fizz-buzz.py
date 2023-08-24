class Solution:
    def __init__(self):
        words = {
            3: 'Fizz',
            5: 'Buzz',
            15: 'FizzBuzz'
        }
        self.words = sorted(words.items(), reverse=True, key=lambda x: x[0])
    
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            for num, word in self.words:
                if i % num == 0:
                    s = word
                    break
            else:
                s = str(i)
            res.append(s)
        return res