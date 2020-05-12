'''
Flood Fill
Solution
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
   Show Hint #1
Python3
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack=[]
        tt=[]
        x=len(image)
        t=image[sr][sc]
        stack.append([sr,sc])
        while(len(stack)!=0):
            l=stack.pop()
            k=[l[0],l[1]]
            if k not in tt:
                tt.append(k)
                a = l[0]
                b = l[1]
                try:
                    if image[a][b] == t:
                        image[a][b] = newColor
                        if (0 <= (a + 1) < x and 0 <= b <= x):
                            if image[a + 1][b] == t:
                                stack.append([a + 1, b])
                        if (0 <= (a - 1) < x and 0 <= b <= x):
                            if image[a - 1][b] == t:
                                stack.append([a - 1, b])
                        if (0 <= a < x and 0 <= (b + 1) <= x):
                            if image[a][b + 1] == t:
                                stack.append([a, b + 1])
                        if (0 <= a < x and 0 <= (b - 1) <= x):
                            if image[a][b - 1] == t:
                                stack.append([a, b - 1])


                except:
                    pass



        return image


'''