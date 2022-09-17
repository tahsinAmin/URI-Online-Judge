nums = [2, 7, 11, 15]
target = 9
i, j = 0, 1
while i < len(nums):
    while j < len(nums):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
        j += 1
    i += 1
