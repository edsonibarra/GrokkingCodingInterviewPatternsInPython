def three_sum(nums: list[int], target: int) -> bool:
    nums.sort()
    for i in range(0, len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            triplet = nums[i] + nums[left] + nums[right]
            if triplet == target:
                print("Triplet found", nums[i], nums[left], nums[right])
                return True
            elif triplet > target:
                right -= 1
            else:
                left += 1
    print("triplet not found")
    return False


def main():
    result = three_sum([1, 2, 3, 4, 5, 6], 12)
    print(result)


if __name__ == "__main__":
    main()
