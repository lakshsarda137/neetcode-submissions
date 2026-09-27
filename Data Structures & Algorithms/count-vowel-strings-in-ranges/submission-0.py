class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vowels = {'a', 'e', 'i', 'u', 'o'}
        status = [False] * len(words)
        for idx in range(len(words)):
            word = words[idx]
            if word[0] in vowels and word[-1] in vowels:
                status[idx] = True

            # else:
            #     status[idx] = False


        for idx in range(len(queries)):
            query = queries[idx]
            count = 0
            start = query[0]
            end = query[1]

            for inner_idx in range(start, end + 1, 1):
                if status[inner_idx]:
                    count += 1

            result.append(count)
        
        return result
