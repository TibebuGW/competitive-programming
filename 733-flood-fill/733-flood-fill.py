class Solution:
    def floodFill(self, image: List[List[int]], r: int, c: int, newColor: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        inbound = lambda row, col: 0 <= row < n and 0 <= col < m
        b = [[0,-1], [0,1], [1,0], [-1,0]]
        if image[r][c] == newColor:
            return image
        temp = image[r][c]
        image[r][c] = newColor
        
        def dfs(sr, sc):
            image[sr][sc] = newColor
            for i in range(len(b)):
                if inbound(sr+b[i][0], sc+b[i][1]) and image[sr+b[i][0]][sc+b[i][1]] == temp:
                        dfs(sr+b[i][0], sc+b[i][1])
        
        dfs(r,c)
        return image
                
        
        