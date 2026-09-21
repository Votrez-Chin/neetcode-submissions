class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        rev = nums[::-1]
        left = [1]
        rigt = [1]
        leftprod = 1
        rigtprod = 1
        prod = 1
        for i in range(len(nums)-1):
            rigtprod *= rev[i]
            leftprod *= nums[i]
            rigt.append(rigtprod)
            left.append(leftprod)
        rerigt = rigt[::-1]
        for a,b in zip(left,rerigt):
            output.append(a*b)
        return output