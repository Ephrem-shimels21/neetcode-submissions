class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        store = {}

        for num in nums:
            if num in store.keys():
                return True
            else:
                store[num] = 1
        return False
        