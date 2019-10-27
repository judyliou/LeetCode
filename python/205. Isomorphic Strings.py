# Solution 1: Brute-force
def isIsomorphic(self, s, t):
        if len(s) != len(t):
                return False
            
        table = {}
        num = 0
        s2, t2 = '', ''
        for i in range(len(s)):
            if s[i] in table:
                trans = table[s[i]]
            else:
                trans = num
                table[s[i]] = num
                num += 1
            s2 += str(trans)
        table = {}   
        num = 0
        for i in range(len(t)):
            if t[i] in table:
                trans = table[t[i]]
            else:
                trans = num
                table[t[i]] = num
                num += 1
            t2 += str(trans) 
        return s2 == t2
     
        
# Solution 2: Break earlier
def isIsomorphic(self, s, t):
    if len(s) != len(t):
            return False

    table1, table2 = {}, {}
    num1, num2 = 0, 0
    s2, t2 = '', ''
    for i in range(len(s)):
            if s[i] in table1 and t[i] in table2:
                    if table1[s[i]] != table2[t[i]]: return False
            elif table1.get(s[i], None) != table2.get(t[i], None): return False
            else: # both are not in
                    table1[s[i]] = num1
                    table2[t[i]] = num2
                    num1 += 1
                    num2 += 1
    return True
    
    
# Solution 3: Match char directly
def isIsomorphic(self, s, t):
    if len(s) != len(t):
            return False

    table = {}
    for i in range(len(s)):
            if s[i] in table:
                    if table[s[i]] != t[i]: return False
            else:
                    if t[i] in table.values(): return False
                    else:
                            table[s[i]] = t[i]
    return True
