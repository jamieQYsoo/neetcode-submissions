class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dictionary = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in num_dictionary:
                return [num_dictionary[diff], index]
            num_dictionary.update({value : index})