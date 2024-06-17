# Basic example two pointers

def two_pointers(nums: list[int]) -> None:
    """
    Basic example of two pointers pattern.
    """
    left: int = 0
    right: int = len(nums) - 1
    print(nums)
    while left <= right:
        print(f"Left={nums[left]}, Right={nums[right]}")
        left += 1
        right -= 1

def main():
    nums = [1, 2, 3, 4, 5]
    two_pointers(nums)


if __name__ == "__main__":
    main()
