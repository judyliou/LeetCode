class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        simplified = []
        for i in path.split('/'):
            if i == '.' or i == '':
                continue
            elif i == '..':
                if simplified:
                    simplified.pop()
            else:
                simplified.append(i) 
        return '/' + '/'.join(simplified)
