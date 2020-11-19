import math
import time


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:

        start = time.time()

        L = int(L)
        R = int(R)
        count = 0

        for i in range(R, L-1, -1):
            if self.isPalindrom(i):
                squareRoot = math.sqrt(i)
                if squareRoot.is_integer() and self.isPalindrom(int(squareRoot)):
                    print(i)
                    count += 1

        end = time.time()
        print(end - start)

        print(count)
        return count

    @ staticmethod
    def isPalindrom(num: int) -> bool:
        if num < 10:
            return True

        num = str(num)

        for i in range(len(num)//2):
            if num[i] != num[Solution.getNegIdx(i)]:
                return False
        return True

    @ staticmethod
    def getNegIdx(num: int) -> int:
        return -(num + 1)


tmp = Solution()
tmp.superpalindromesInRange("92904622", "232747148")
