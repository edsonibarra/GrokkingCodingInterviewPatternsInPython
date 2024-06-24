def two_sum(nums: list[int], target: int):
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        result = nums[left] + nums[right]
        if result == target:
            return [left, right]
        elif result < target:
            left += 1
        else:
            right -= 1
    return -1


def main():
    nums = [1,2,3,4,5,6]
    target = 9
    print(two_sum(nums, target))
    print(two_sum(nums, 10000))


if __name__ == "__main__":
    main()
