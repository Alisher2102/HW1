def findLengthOfLCIS(self, nums: List[int]) -> int:
        
    db = [1] * len(nums)

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            db[i] = db[i-1]+1
        
    return max(db)