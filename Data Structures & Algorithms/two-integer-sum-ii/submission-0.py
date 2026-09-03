class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        flag = False

        while not flag:
            left_num = numbers[left]
            right_num = numbers[right]

            if left_num + right_num == target:
                flag = True
                return [left + 1, right + 1]

            elif left_num + right_num < target:
                left += 1

            elif left_num + right_num > target:
                right = right - 1

        