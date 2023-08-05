class Solution:
    def isValid(self, s: str) -> bool:
        op = []
        mapping = {'(':')', '[':']', '{':'}'}
        for p in s:
            if p in mapping.keys():
                op.append(p)
            elif p in mapping.values():
                if op and (op[-1] == mapping[p]):
                    op.pop()
                else:
                    return False
            else:
                return False   
        
        return len(op) == 0


s = Solution()
s.isValid("(}")