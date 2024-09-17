# Problem :- https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

# Solution :- https://www.youtube.com/watch?v=dxhw7xx2fkE&ab_channel=devWithArsalan

# Uncommon Words from Two Sentences(884)

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s3 = s1 +' ' + s2
        lis = []
        s3 = s3.split()
        for word in set(s3):
            if (s3.count(word) == 1):
                lis.append(word)
        return lis
