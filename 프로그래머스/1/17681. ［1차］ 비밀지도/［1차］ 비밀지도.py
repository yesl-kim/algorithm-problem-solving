def solution(n, arr1, arr2):
    def decrypt(num):
        def to_binary_str(num):
            if num < 2:
                return str(num)
            
            share, rest = divmod(num, 2)
            return to_binary_str(share) + str(rest)
        
        return to_binary_str(num).zfill(n)
    
    def overlap(str1, str2):
        row = ''
        for i in range(n):
            row += ' ' if str1[i] == '0' and str2[i] == '0' else '#'
        return row
    
    return [overlap(decrypt(a), decrypt(b)) for a, b in zip(arr1, arr2)]
            
    