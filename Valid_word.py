class Solution:
    def isValid(self, word: str) -> bool:
        
        if len(word) < 3:
            return False

        vowels ='aeiou' 
        vowels += vowels.upper() 
        consonants ='qwrtypsdfghjklzxcvbnm' 
        consonants += consonants.upper()
        has_vowel = False
        has_consonant = False

        for c in word:
            
            if not c.isalnum():
                return False

            
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    
                    has_consonant = True

        
        return has_vowel and has_consonant