from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    my_list.pop(index)
    return my_list


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    x = len(my_list)

    while n > 0:
        my_list.pop(x - 1)
        x -= 1
        n -= 1
    return my_list


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))
