class Solution(object):
    def maxArea(self, array):
        area = 0
        max_area = 0
        i = 0
        j = len(array) - 1
        while i < j:
            area = max(min(array[i], array[j]) * (j - i), area)
            if array[j] >= array[i]:
                i += 1
            else:
                j -= 1
        return area


if __name__ == "__main__" :
    hist_Area = Solution()
    hist = [2,5,4,5,1]
    print hist_Area.maxArea(hist)