class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []
        if not numbers:
            return result

        temp = 0

        while left <= right:
            temp = numbers[left] + numbers[right]
            if temp > target:
                right -= 1
            elif temp < target:
                left +=1
            else:
                result.append(left + 1)
                result.append(right + 1)
                break
        return result