



class Solution:

    def reverseString(self, s:list[str]):
        s = input().split()
        j = len(s) - 1
        for i in range(len(s)):
            s.append(s[j])
            s.pop(j)
            j-=1

        print(s)
        # I choosed to go with this soultion to maxmize the space complixity and go with O(1)





a = input().split()
print(a)
j = len(a) - 1 
for i in range(len(a)):
    print('j is:',j) # very good job at debuging using these methods:)
    a.append(a[j])
    a.pop(j)
    j-=1
    print(a,j,a[j]) #  method number 2 

print(a)

