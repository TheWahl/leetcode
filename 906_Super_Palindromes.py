import math
import time


class Solution:

    def superpalindromesInRange(self, L: str, R: str) -> int:

        L = int(math.ceil(math.sqrt(int(L))))
        R = int(math.floor(math.sqrt(int(R))))

        halfL = 1  # L if L < 10 else int(
        # L / (10 ** math.floor((int(math.log10(L))+1) / 2)))

        count = 0
        removed = 0
        while(True):
            palins = self.createPalindrom(halfL)

            for i in reversed(palins):
                if i < L:
                    palins.remove(i)
                elif i > R:
                    palins.remove(i)
                    removed += 1
            if removed == 2:
                break
            elif not palins:
                removed = 0
                halfL += 1
                continue
            else:
                removed = 0

            for i in palins:
                if self.isPalindrom(i):
                    if self.isPalindrom(i**2):
                        count += 1

            halfL += 1

        return count

    @staticmethod
    def rev(num):
        return int(num != 0) and ((num % 10) *
                                  (10**int(math.log(num, 10))) +
                                  Solution.rev(num // 10))

    @staticmethod
    def isPalindrom(num):
        return num == Solution.rev(num)

    @staticmethod
    def createPalindrom(n):

        if n < 10:
            return [n, n * 11]

        out1 = (n * 10**int(math.log10(n)+1)) + Solution.rev(n)
        out2 = (n * 10**int(math.log10(n//10)+1)) + Solution.rev(n // 10)

        return [out1, out2]


tmp = Solution()
tmp.superpalindromesInRange("1", "999999999999999999")
