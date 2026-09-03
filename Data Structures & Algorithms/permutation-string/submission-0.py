class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h1 = {}
        h2 = {}
        A, B = len(s1), len(s2)
        for s in s1:
            if s in h1:
                h1[s] += 1

            else:
                h1[s] = 1

        left = 0

        for right in range(left, len(s2), 1):
            if s2[right] in h2:
                h2[s2[right]] += 1

            else:
                h2[s2[right]] = 1
            if (right - left + 1) == A:
                if h1 == h2:
                    return True

                else:
                    h2[s2[left]] -= 1
                    if h2[s2[left]] == 0:
                        del h2[s2[left]]
                    left = left + 1

        return False

        