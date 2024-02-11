class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for char in s:
            if char.isalnum():
                new.append(char.lower())
        for i in range(int(len(new)/2)):
            if new[i] != new[len(new)-i-1]:
                return False
        return True
