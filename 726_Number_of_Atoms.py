class Solution:
    
    def countOfAtoms(self, formula: str) -> str:

        multiplier = 1
        
        cur = ""
        i = 0

        elements = {}
        
        while i < len(formula):
            if formula[i].isalpha():
                cur, i = self.grabName(i, formula)                
                number, i = self.grabNumber(i, formula)
                
                if cur in elements:
                    elements[cur] += number * multiplier
                else:
                    elements[cur] = number * multiplier

            elif formula[i] is '(':
                multiplier = self.addMultiplier(i, formula, multiplier)
            elif formula[i] is ')':
                multiplier, i = self.removeMultiplier(i, formula, multiplier)

        print(elements)
                
    #idx is index immediatley before there is a suspected number
    @staticmethod
    def grabName(idx, ar): 
        name = ar[idx]
        idx += 1
        
        while idx < len(ar) and ar[idx].islower():
            name += ar[idx]
            idx += 1
            
        return name, idx
        
    @staticmethod
    def grabNumber(idx, ar): 
        if idx < len(ar) and ar[idx].isdigit():
            num = ar[idx]
            idx += 1
            
            while idx < len(ar) and ar[idx].isdigit():
                num += ar[idx]
                idx += 1
            
            return num, idx
        else:
            return 1, idx
        
    @staticmethod
    def addMultiplier(idx, ar, multiplier):
        count = 0
        while idx < len(ar):
            if ar[idx] is '(':
                count += 1
            elif ar[idx] is ')':
                if count is 0:
                    idx += 1
                    break
                else:
                    count -= 1
            idx += 1
        
        tmpMult, i = Solution.grabNumber(idx, ar)
        multiplier *= tmpMult
        return multiplier
        
    @staticmethod
    def removeMultiplier(idx, ar, multiplier):
        idx += 1
        tmpMult, idx = Solution.grabNumber(idx, ar)
        multiplier /= tmpMult
        return multiplier, idx
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    