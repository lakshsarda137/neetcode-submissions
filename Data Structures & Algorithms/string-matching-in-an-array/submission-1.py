class Solution:



    def stringMatching(self, words: List[str]) -> List[str]:
        def helper(word1, word2):
            p1, p2 = 0, 0

            while p1 < len(word1) and p2 < len(word2):
                c1, c2 = word1[p1], word2[p2]
                if p1 == 0 and (c1 != c2):
                    p2 += 1
                elif c1 != c2:
                    p1 = 0
                elif c1 == c2:
                    p1 += 1
                    p2 += 1
            
            if p1 == len(word1):
                return True

            return False


        res = []
        set_of_words = set()
        for i in range(len(words)):

            for j in range(len(words)):

                if i != j:
                    if helper(words[i], words[j]) and words[i] not in set_of_words:
                        res.append(words[i])
                        set_of_words.add(words[i])
        
        return res



        