class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_charCountMap = {}
        guess_charCountMap = {}

        for x in secret:
            if x not in secret_charCountMap:
                secret_charCountMap[x] = 1
            else:
                secret_charCountMap[x] += 1
        for y in guess:
            if y not in guess_charCountMap:
                guess_charCountMap[y] = 1
            else:
                guess_charCountMap[y] += 1
        
        bulls = 0
        cows = 0
        for i in range(len(secret) | len(guess)):
            if secret[i] == guess[i]:
                secret_charCountMap[secret[i]] -= 1
                guess_charCountMap[guess[i]] -= 1
                bulls += 1
        
        for x in guess_charCountMap:
            if x in secret_charCountMap:
                cows += min(secret_charCountMap[x], guess_charCountMap[x])
        
        return f"{bulls}A{cows}B"