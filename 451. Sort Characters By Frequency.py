class Solution:
    def frequencySort(self, s: str) -> str:
        map = {}
        finalString = ''
        # created a hash map char and it's count
        for char in s:
            if char not in map.keys():
                map[char] = 1
            else:
                map[char] += 1
        # sort the hash map by the largest value first
        new_map = dict(sorted(map.items(), key=lambda x:x[1],reverse=True))
        # loop on items to make the final string
        for item,value in new_map.items():
            # ljust method put a string K for N times , with first arg as the count and the second the string!
            # we will make use of that one!
            finalString += ''.ljust(value,str(item))
        return finalString


s = Solution()
print(s.frequencySort('attack'))