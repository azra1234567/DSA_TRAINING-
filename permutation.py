class Solution:
    def permute(self, nums):

        result = [[]]

        for num in nums:
            new_list = []

            for perm in result:
                for i in range(len(perm) + 1):
                    new_list.append(perm[:i] + [num] + perm[i:])

            result = new_list

        return result