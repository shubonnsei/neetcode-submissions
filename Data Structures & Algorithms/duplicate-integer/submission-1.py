class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkin = set()
        for num in nums:
            if num in checkin:
                return True
            checkin.add(num)
        return False