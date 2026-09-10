class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        key = 0
        for i in nums:
            key = i
            if key in groups:
                groups[key] += 1
            else:
                groups[key] = 1
        sort_grps = sorted(groups.items(), key = lambda x:x[1])
        sort = sort_grps[::-1]
        ans = []
        for j in range(k):
            ans.append(sort[j][0])
        return ans
        
        
        