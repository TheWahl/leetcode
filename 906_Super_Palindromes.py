import math
from math import ceil
import time


class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:

        start = time.time()

        L = str(math.ceil(math.sqrt(int(L))))
        R = str(math.floor(math.sqrt(int(R))))

        if L == R:
            R = self.addOne(R)

        count = 0
        halfL = L if len(L) == 1 else self.intToString(
            self.stringToInt(L[:ceil(len(L) / 2)])-1)

        while (True):

            newPalindroms = self.createPalindrome(halfL)  # Create palindroms
            halfL = self.addOne(halfL)

            for i in newPalindroms.copy():
                if self.stringCompare(i, L) == -1:
                    newPalindroms.remove(i)
            if not newPalindroms:
                continue

            for i in newPalindroms.copy():
                if self.stringCompare(i, R) == 1:
                    newPalindroms.remove(i)
            if not newPalindroms:
                break

            print(newPalindroms)

            for i in newPalindroms:
                square = self.intToString(self.stringToInt(i) ** 2)

                if self.isPalindrom(square):
                    count += 1
                    print(i)

        end = time.time()
        print(end - start)  # 71.6667218208313
        print(count)
        return count

    @ staticmethod
    def isPalindrom(str: str) -> bool:

        for i in range(len(str)//2):
            if str[i] != str[Solution.getNegIdx(i)]:
                return False
        return True

    @ staticmethod
    def getNegIdx(num: int) -> int:
        return -(num + 1)

    @staticmethod
    def createPalindrome(string: str) -> [str]:

        reverse1 = ''
        reverse2 = ''
        for i in range(len(string)):
            reverse1 += string[Solution.getNegIdx(i)]
            if i != 0:
                reverse2 += string[Solution.getNegIdx(i)]

        return [string + reverse1, string + reverse2]

    @staticmethod
    def intToString(num: int) -> str:
        newNum = ''
        while(num > 0):
            lastDigit = num % 10
            switch = {
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5',
                6: '6',
                7: '7',
                8: '8',
                9: '9',
                0: '0'
            }
            newNum = switch.get(lastDigit) + newNum
            num = int(num / 10)
        return newNum

    @staticmethod
    def stringToInt(str: str) -> int:
        num = 0
        factor = 1

        for i in range(len(str)-1, -1, -1):
            switch = {
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '0': 0
            }

            num += switch.get(str[i]) * factor

            factor *= 10
        return num

    """ 
    This method takes in a string representing an integer and adds one to it.
    """
    @staticmethod
    def addOne(numStr: str) -> str:
        newStr = ''

        for i in range(len(numStr)-1, -1, -1):
            carry = False
            if numStr[i] == '0':
                newStr = '1' + newStr
            elif numStr[i] == '1':
                newStr = '2' + newStr
            elif numStr[i] == '2':
                newStr = '3' + newStr
            elif numStr[i] == '3':
                newStr = '4' + newStr
            elif numStr[i] == '4':
                newStr = '5' + newStr
            elif numStr[i] == '5':
                newStr = '6' + newStr
            elif numStr[i] == '6':
                newStr = '7' + newStr
            elif numStr[i] == '7':
                newStr = '8' + newStr
            elif numStr[i] == '8':
                newStr = '9' + newStr
            elif numStr[i] == '9':
                newStr = '0' + newStr
                carry = True

            if not carry:
                newStr = numStr[0:i] + newStr
                break
            elif i == 0:
                newStr = '1' + newStr

        return newStr

    @staticmethod
    def stringCompare(a, b):
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            for i in range(len(a)):
                if a[i] < b[i]:
                    return -1
                elif a[i] > b[i]:
                    return 1
            return 0


tmp = Solution()
tmp.superpalindromesInRange("1", "2")
