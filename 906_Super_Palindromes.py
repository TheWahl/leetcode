import * from math as math


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        L = int(L)
        R = int(R)
        count = 0

        for i in range(R+1, L, -1):
            if self.isPalindrom(i):
                squareRoot = math.sqrt(i)
                if self.isPalindrome(squareRoot):
                    count += 1

        print(count)

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
tmp.superpalindromesInRange("4", "1000")
