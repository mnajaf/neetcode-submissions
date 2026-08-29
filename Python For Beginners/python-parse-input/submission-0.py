from typing import List

def read_integers() -> List[int]:
    user = input()

    x = user.split(",")
    for i in range(len(x)):
        x[i] = int(x[i])

    return x

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
