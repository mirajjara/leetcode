# Miraj Jara - October 15, 2024
# Permutation In String
# Medium problem
# https://leetcode.com/problems/permutation-in-string/

# sort the first string (substring)
# loop through the second string with a sliding window the length of the substring
# each iteration, sort the winodw and check if they match

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_substring = sorted(s1)
        r = len(s1)
        
        for l in range(len(s2)):
            
            sorted_section = sorted(s2[l:r])
            
            if sorted_substring == sorted_section:
                return True
            
            r += 1
        
        return False
    
#this solution is really ineffecient in both time and space im so sorry