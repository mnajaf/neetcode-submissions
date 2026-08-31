from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    new_list = []
    while len(arr) > 0:
        new_list.append(arr.pop())
    return new_list



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
