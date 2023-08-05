class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #storing the nums in a hash table
        d = {}
        for num in nums:
            if num in d.keys(): d[num] += 1
            else: d[num] = 1
        #sort the hash table
        sortedByFreq = sorted(d.items(), key=lambda x: x[1], reverse= True)
        #append the top K most frequent numbers to the answer list
        ans = []
        for i in range(k):
            ans.append(sortedByFreq[i][0])
        
        
        return ans
s = Solution()
s.topKFrequent([1,1,1,2,2,3],4)