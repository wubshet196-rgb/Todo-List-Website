def canReach(nums, start):
    visited = set()

    def dfs(index):
        if index < 0 or index >= len(nums) or index in visited:
            return False
        if nums[index] == 0:
            return True
        
        visited.add(index)
        return dfs(index + nums[index]) or dfs(index - nums[index])

    return dfs(start)


nums = [4, 2, 3, 0, 3, 1, 2]
start = 5
print(canReach(nums, start))  
