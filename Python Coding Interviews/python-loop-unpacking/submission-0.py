from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    kid = 0
    max = 0
    for name,score in scores:
        if max < score:
            max = score
            kid = name
    return kid


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
