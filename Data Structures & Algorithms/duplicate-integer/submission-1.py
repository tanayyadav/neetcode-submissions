class Solution:
    def hasDuplicate(self, nums):
        n = len(nums)

        my_set=set(nums)

        m = len(my_set)

        if m < n:
            return True
        else:
            return False