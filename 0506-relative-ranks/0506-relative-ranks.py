class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rankings = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        ranks = { score: rankings[i] 
                 if i < len(rankings) else str(i + 1) 
                 for i, score 
                 in enumerate(sorted(score, reverse=True)) }
        
        return [ranks[s] for s in score]