# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation

class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

class anothersolution:
    def rotate(self,matrix:list) -> None:
        matrix[:] = zip(*matrix[::-1])
        

m = anothersolution()
m.rotate( [[1,2,3],[4,5,6],[7,8,9]])

m = [ [1,2,3],[4,5,6],[7,8,9]]
print(zip(m))
print(*m)
m[:]=zip(*m[::-1])
print(m)

"""
https://leetcode.com/problems/rotate-image/solutions/18884/seven-short-solutions-1-to-7-lines/?orderBy=most_votes

Thank you! And for those who can't understand the most pythonic version, here I am:
First we use slice to turn it upside down
In Python, to slice a list : [start:stop:step]

So if we use [::-1], it's like stepping backwards, the last list will be the first, thus turning the matrix upside down

Then we will use zip function to transpose the matrix@James Rettie
In python, * is the splat operator. It is used for unpacking a list into arguments. For example: foo(*[1, 2, 3]) is the same as foo(1, 2, 3).
The zip() function takes n iterables, and returns y tuples, where y is the least of the length of all of the iterables provided.
For example:
zip(['a', 'b', 'c'], [1, 2, 3])
Will yield
('a', 1) ('b', 2) ('c', 3)
So calling A = zip(*A) is returning:
A= [[1, 2, 3], [4, 5, 6],[7, 8, 9,]]
So zip(*A) is the same as calling zip([1, 2, 3], [4, 5, 6],[7, 8, 9,])
It will yield:

      (1, 4, 7)
      (2, 5, 8)
      (3, 6, 9)
[[1st in 1st list, 1st in 2nd list,....], [2nd in 1st list, 2nd in 2nd list....], ....]
It's exactly like transposing the matrix. How brilliant!

And for the A[:] part, the difference is you are making a copy of the entire list
If you only use A = zip(*A[::-1]), you just make A point to the new list
If you use A[:] = zip(*A[::-1]), you actually assign the value to your A, which is what we want."""