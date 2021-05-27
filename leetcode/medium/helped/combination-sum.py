#https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates, target: int):
        # O(n logn) where n = len(candidates)
        candidates.sort()
        # O(# of combos) space
        dp = []
        
        # O(target * len(candidates) * max(len(combo) for combo in dp))
        for t in range(1,target+1):
            new_dp = []
            # O(len(candidates))
            for c in candidates:
                if c > t: #not matches
                    break
                if c < t: 
                    complementPresent = t-c-1 >= 0
                    if complementPresent:
                        adds = []
                        # O(max(len(combo) for combo in dp))
                        for combo in dp[t-c-1]:
                            cIsGreatestElementInOldCombo = c >= combo[-1]
                            if cIsGreatestElementInOldCombo:
                                adds.append(combo + [c])
                        new_dp.extend(adds)
                else: 
                    new_dp.append([c])
            dp.append(new_dp)
        return dp[target-1]
print(Solution().combinationSum([2,3,6,7], 7))