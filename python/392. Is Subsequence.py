def isSubsequence(self, s, t):
        p1, p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        return p1 == len(s) 


def isSubsequence(self, s, t):
        t_map = {}
        for i in range(len(t)):
            if t[i] in t_map:
                t_map[t[i]].append(i)
            else:
                t_map[t[i]] = [i]
        
        prev = -1
        for i in s:
            if i not in t_map:
                return False
            else:
                flag = 0
                for num in t_map[i]:
                    if num > prev:
                        flag = 1
                        break
                if flag == 1:
                    prev = num
                else: return False
        return True
