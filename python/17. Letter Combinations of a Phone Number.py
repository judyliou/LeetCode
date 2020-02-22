def letterCombinations(self, digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == '':
        return []

    letter = {'2': ['a','b','c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'],
                '6': ['m','n','o'], '7': ['p','q','r','s'], '8': ['t','u','v'], '9': ['w','x','y', 'z']}
    ans = ['']
    for i in digits:
        l = letter[i]
        temp = []
        for j in l:
            temp.extend([prev + j for prev in ans])
        ans = temp
    return ans
