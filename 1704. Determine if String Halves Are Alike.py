class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length = len(s)//2
        # print('length : ', length)
        a = s[:length]
        b = s[length:]
        # print(f'a is {a} and b {b}')
        count_a = 0
        count_b = 0
        for char_a in a:
            if char_a in vowels:
                count_a += 1
        for char_b in b:
            if char_b in vowels:
                count_b += 1

        if count_a == count_b:
            print('equal')
            return True
        else:
            print('False')
            return False

s = Solution()

s.halvesAreAlike('attack')