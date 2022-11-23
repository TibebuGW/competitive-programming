class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        visited = set()
        
        def backtrack(visited_indices = set(), path = ""):
            if len(visited_indices) == len(tiles):
                return
            
            for i in range(len(tiles)):
                if i not in visited_indices:
                    visited_indices.add(i)
                    visited.add(path+tiles[i])
                    backtrack(visited_indices, path+tiles[i])
                    visited_indices.remove(i)
        
        backtrack()
        return len(visited)