class Solution(object):
    def firstUniqChar(self, s):
        exist = ''
        not_repeat = {}
        for i in range(len(s)):
            if s[i] not in exist:
                exist += s[i]
                not_repeat[s[i]] = i
            else:
                if s[i] in not_repeat:
                    del not_repeat[s[i]]
        if len(not_repeat) == 0:
            return -1
        else:
            return min(not_repeat.values())
