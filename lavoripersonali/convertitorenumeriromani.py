
class Solution(object):
    
    def __init__(self):
        self.numeriromani = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
    
    def romanToInt(self, s):
        total = 0
        n = len(s)
        
        for i in range(n):
            numero_attuale = self.numeriromani[s[i]]
            
            if i + 1 < n and numero_attuale < self.numeriromani[s[i + 1]]:
                total -= numero_attuale
            else:
                total += numero_attuale
        
        return total
        