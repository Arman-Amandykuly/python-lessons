class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        mx = 0
        for i in gain:
            h+=i
            mx = max(h,mx)
        return mx