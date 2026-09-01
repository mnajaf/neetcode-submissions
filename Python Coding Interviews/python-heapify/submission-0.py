import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heapq.heapify(strings)
    
    return strings


def heapify_integers(integers: List[int]) -> List[int]:
    heapq.heapify(integers)

    return integers


def heap_sort(nums: List[int]) -> List[int]:
    nums.sort()
    return nums


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
