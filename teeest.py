class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        counter = 0
        broken_set = set(brokenLetters)


        print(words)
