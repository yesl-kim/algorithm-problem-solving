def solution(enroll, referral, seller, amount):
    ans = [0] * len(enroll)
    indices = { name: i for i, name in enumerate(enroll)}
    
    def share(i, sales):
        if i is None or not sales:
            return
        
        shares = sales // 10
        profit = sales - shares
        ans[i] += profit
        share(indices.get(referral[i]), shares)
        
    
    for s, x in zip(seller, amount):
        share(indices[s], x * 100)
    
    return ans