def find_pairs_with_sum(nums, target_sum):
    index_pairs = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target_sum:
                index_pairs.append((i,j))
    return index_pairs

nums = [4,2,3]
target = 6
a = find_pairs_with_sum(nums,target)
print(a)