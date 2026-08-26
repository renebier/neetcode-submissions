class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = list()
        s = 1
        def recalcPostfix(index):
            n=1
            for i in range(index,len(nums)):
                n *= nums[i]
            return n
        postfix = recalcPostfix(1)
        prefix = 1
        out.append(postfix)
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            if nums[i] == 0:
                postfix = recalcPostfix(i+1)
            else:
                postfix /= nums[i]
            out.append(int(prefix*postfix))
        return out

            