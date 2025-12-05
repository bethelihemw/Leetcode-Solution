class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0
        target = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                time_contributed = min(tickets[i], target)
            else:
                rounds_completes = target - 1
                
                time_contributed = min(tickets[i],rounds_completes)
            
            total_time += time_contributed
            
        return total_time