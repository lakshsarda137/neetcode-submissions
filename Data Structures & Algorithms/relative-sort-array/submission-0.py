class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        hash_table = {}
        for num in arr1:
            if num not in hash_table:
                hash_table[num] = 1

            else:
                hash_table[num] += 1

        final = []
        used = set()
        for num in arr2:
            
            for _ in range(hash_table[num]):
                final.append(num)
                used.add(num)
        new = []
        for num in arr1:
            if num not in used:
                for _ in range(hash_table[num]):
                    new.append(num)
                    used.add(num)
        new.sort()
        final = final + new.copy()
        return final
        