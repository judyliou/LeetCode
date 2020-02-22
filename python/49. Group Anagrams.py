class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            s_sort = ''.join(sorted([i for i in s]))
            if s_sort in d:
                d[s_sort] += [s]
            else:
                d[s_sort] = [s]
        rtn = []
        for v in d.values():
            rtn.append(v)
        return rtn
