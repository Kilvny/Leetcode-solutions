"""
# cheatsheet : 
- using dfs
- prefix and suffix from wordSet

"""

class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        res = []
        for i in range(len(words)):
            word = wordcpy = words[i]
            words.remove(words)
            for subs in words:
                if word == "":
                    res.append(wordcpy)
                    break
                if subs in word:
                    word = word.replace(subs, '')
                    if word == "":
                        res.append(wordcpy)
                        break
            words.insert(i, word)
        return res

class CorrectSolution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        wordSet = set(words)

        def dfs(word):
            for i in range(len(word)):
                prefix = word[:i] # word from the beginning till the i but not including i
                suffix = word[i:] # word from the i till the end including i
                if prefix in wordSet and suffix in wordSet:
                    return True
                if prefix in wordSet and dfs(suffix): # if the first part is a word in wordset and the second part can conacnate words too 
                    return True

        res = [] 
        for word in words:
            if dfs(word):
                res.append(word)
        return res









# word = 'catdog'
words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
res = []
for i in range(len(words)):
    word = words[i]
    wordcpy = words[i]
    words.remove(word)
    for subs in words:
        if word == "":
            res.append(wordcpy)
            break
        if subs in word:
            word = word.replace(subs,'')
            if word == "":
                res.append(wordcpy)
                break
    words.insert(i,word)
print(res)

# if 'cat' in word or 'dog' in word:
#     print(True)
#     word = word.replace('cat','')
#     if 'cat' in word or 'dog' in word:
#         word = word.replace('dog','')
#         print(f'Second True')
#     else:
#         print(f'second False')
#     if 'cat' in word or 'dog' in word:
#         print(word)
#         print('third True')
#     else:
#         print('third false')
# else:
#     print(False)




# wordSet = set(words)

# def dfs(word):
#     for i in range(len(word)):
#         prefix = word[:i]
#         suffix = word[i:]
#         if (prefix in wordSet and suffix in wordSet ) or ( prefix in wordSet and dfs(suffix)):
#             return True

# res = []
# for w in words:
#     if dfs(w):
#         res.append(w)
# return res