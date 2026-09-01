from typing import List, Set


def double_nums(nums: List[int]) -> Set[int]:
    s = {2 * num for num in nums}

    return s


# do not modify below this line

output1 = double_nums([1, 2, 3])
print(type(output1)) 
print(sorted(list(output1)))

output2 = double_nums([4, -2, 0, 7])
print(type(output2)) 
print(sorted(list(output2)))

output3 = double_nums([10, 20, 30, 40, 50])
print(type(output3)) 
print(sorted(list(output3)))
