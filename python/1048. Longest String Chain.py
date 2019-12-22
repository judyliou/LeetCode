def longestStrChain(self, words):         
        words.sort(key = len)
        dp = {} 
        res = 0 
        for word in words:
            cur_max = 0 
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                if pred in dp:
                    cur_max = max(cur_max, dp[pred])
            dp[word] = cur_max + 1
            res = max(res, dp[word])
        return res
            
def longestStrChain(self, words):
    words.sort(key=len)
    word_len = {}
    word_to_index = {}
    dp = [0] * len(words)

    for i in range(len(words)):
        word = words[i]
        word_len[len(word)] = word_len.get(len(word),[]) + [word]
        word_to_index[word] = i

    for i in range(len(words)):
        word = words[i]
        if word_len.get(len(word)-1) == None:
            dp[i] = 1
        else:
            M = 0
            for j in range(len(word)):
                word_from = word[:j] + word[j+1:]
                if word_from in word_len[len(word)-1]:
                    M = max(dp[word_to_index[word_from]], M)
            dp[i] = M + 1

    return max(dp)
