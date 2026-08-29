from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    counter = 0

    for num in nums:
        if num == x:
            counter +=1
    return counter



# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
