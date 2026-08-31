from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    return sum(triplet)


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    return box_dimensions[0] * box_dimensions[1] * box_dimensions[2]
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))
