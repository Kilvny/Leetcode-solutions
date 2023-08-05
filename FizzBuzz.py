class Solution:  # faster than 7% and better with space than 85.41%
    def fizzBuzz(self, n: int) -> list[str]:
        mylist = []
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 == 0 and (i != 0):
                mylist.append('FizzBuzz')
            elif (i+1)%3 == 0 and (i != 0):
                mylist.append('Fizz')
            elif (i+1)%5 == 0 and (i != 0):
                mylist.append('Buzz')
            else:
                mylist.append(str(i+1))
        return mylist

def fizzBuzz(n): # optimized soultion faster than 92.02% and space is 85.41%
    mylist = []
    i = 1
    while (i<=n):
        if i%3 == 0 and i%5 == 0 :
            mylist.append('FizzBuzz')
        elif i%3 == 0:
            mylist.append('Fizz')
        elif i%5 == 0:
            mylist.append('Buzz')
        else:
            mylist.append(str(i))
        i+=1
        
    return mylist


test = []
test.append(100) 
print(fizzBuzz(150))



"""
Solution before optimization 

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        mylist = []
        for i in range(n):
            if (i+1)%3 == 0 and (i+1)%5 == 0 and (i != 0):
                mylist.append('FizzBuzz')
            elif (i+1)%3 == 0 and (i != 0):
                mylist.append('Fizz')
            elif (i+1)%5 == 0 and (i != 0):
                mylist.append('Buzz')
            else:
                mylist.append(str(i+1))
        return mylist


"""