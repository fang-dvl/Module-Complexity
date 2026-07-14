from typing import List, TypeVar

Number = TypeVar("Number", int, float)


def has_pair_with_sum(numbers: List[Number], target_sum: Number) -> bool:
    """
    Find if there is a pair of numbers that sum to a target value.

    Time Complexity:
    Space Complexity:
    Optimal time complexity:
    """
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target_sum:
    #             return True
    # return False

    seen = set()
    for num in numbers:
        complement = target_sum - num
        if complement in seen:
            return True
        seen.add(num)
    return False