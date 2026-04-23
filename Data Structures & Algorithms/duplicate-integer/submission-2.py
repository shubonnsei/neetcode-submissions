class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        signin = set()

        for num in nums:
            if num in signin:
                return True
            signin.add(num)

        return False