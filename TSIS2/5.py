class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l = list(map(int,str(n)))
        c = 1
        for i in l:
            c*=i
        return c-sum(l)