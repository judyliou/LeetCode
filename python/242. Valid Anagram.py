# Solution 1: O(n^2)
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    char = dict()
    for i in s:
        char[i] = char.get(i, 0) + 1
    for i in t:
        char[i] = char.get(i, -1) - 1
        if char[i] < 0:
            return False
    return True 


# Solution 2: O(nlogn)
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    else:
        return sorted(s) == sorted(t)


# Solution 3: O(n)
def isAnagram(self, s, t):
    if len(s) != len(t):
        return False

    char = dict()
    for i in s:
        char[i] = char.get(i, 0) + 1
    for i in t:
        char[i] = char.get(i, -1) - 1
        if char[i] < 0:
            return False
    return True   
