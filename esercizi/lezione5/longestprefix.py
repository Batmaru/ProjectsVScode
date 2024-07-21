'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.'''

def longestCommonPrefix(strs):
    if strs==[]:
        return ""
    

    prima_stringa = strs[0]

    prefisso_lungo = 0
    lista_senza_primo_elemento= [e for e in strs]
    lista_senza_primo_elemento.pop(0)
    
    for letter in range(len(prima_stringa)):
        for stringa in lista_senza_primo_elemento:
           
            if letter >= len(stringa) or stringa[letter] != prima_stringa[letter]:
                return prima_stringa[:prefisso_lungo]
        
        prefisso_lungo += 1

    return prima_stringa[:prefisso_lungo]

