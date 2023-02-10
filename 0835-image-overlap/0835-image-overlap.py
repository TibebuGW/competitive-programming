class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        img1_list = []
        img2_list = []
        diff_dict = defaultdict(int)
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    img1_list.append((i, j))
                if img2[i][j] == 1:
                    img2_list.append((i, j))
        
        for img1i, img1j in img1_list:
            for img2i, img2j in img2_list:
                diff = (img1i - img2i, img1j - img2j)
                diff_dict[diff] += 1
        
        max_overlap = 0
        for key, val in diff_dict.items():
            max_overlap = max(max_overlap, val)
        
        return max_overlap