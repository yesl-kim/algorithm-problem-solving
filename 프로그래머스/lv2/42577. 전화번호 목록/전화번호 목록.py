def solution(phone_book):
    phone_book.sort(key=len)
    for i, num in enumerate(phone_book):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(num):
                return False
    
    return True
        