from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    my_set = set()
    for n in nums:
        my_set.add(n)
    return my_set

# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
