def solution(n, arr1, arr2):
    bi = lambda x: format(x, 'b').zfill(n)
    map1, map2 = map(bi, arr1), map(bi, arr2)
    
    decrypt = lambda a, b: "#" if any(x == '1' for x in (a, b)) else " "
    decrypted = ["".join(decrypt(c1, c2) 
                         for c1, c2 in zip(row1, row2)) 
                 for row1, row2 in zip(map1, map2)]
    return decrypted
        