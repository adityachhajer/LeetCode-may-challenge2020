class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) <= 1:
            return True

        while dislikes:
            g1 = set()
            g2 = set()
            g1.add(dislikes[0][0])
            g2.add(dislikes[0][1])
            rem = []
            for i in range(1, len(dislikes)):
                a, b = dislikes[i][0], dislikes[i][1]
                if a in g1 and b in g1:
                    return False
                elif a in g2 and b in g2:
                    return False
                elif a in g1 and b in g2:
                    continue
                elif a in g2 and b in g1:
                    continue
                elif a in g1:
                    g2.add(b)
                elif b in g2:
                    g1.add(a)
                elif a in g2:
                    g1.add(b)
                elif b in g1:
                    g2.add(a)
                else:
                    rem.append(dislikes[i])
            dislikes = rem
        return True


