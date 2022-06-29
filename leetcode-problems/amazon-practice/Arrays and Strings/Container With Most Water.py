class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l_index, r_index = 0, len(height) - 1
        area = 0
        
        while (width := r_index - l_index) > 0:
            # width = r_index - l_index
            area = max(area, min(height[l_index], height[r_index]) * width)
            
            if height[r_index] > height[l_index]:
                # r_index -= 1
                l_index += 1
            else:
                # l_index += 1
                r_index -= 1
                
        return area
                
        