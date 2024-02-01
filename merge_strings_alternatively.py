#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
#If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        word1 = list(word1)
        word2 = list(word2)

        merged = ""

        if(len(word1) > len(word2) ):
            for i in range(len(word1)):
                merged += word1[i]
                if(i < len(word2)):
                    merged += word2[i]
        elif(len(word2) > len(word1)):
            for i in range(len(word2)):
                if(i < len(word1)):
                    merged += word1[i]
                
                merged += word2[i]
                
        else:
            for i in range(len(word1)):
                merged += word1[i]
                if(i < len(word2)):
                    merged += word2[i]

        return merged
        
