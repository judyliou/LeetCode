# Sol 1: brute search
# Time complexity: O(m*n); Space complexity: O(1)
def numJewelsInStones(self, J, S):
        count = 0
        for s in S:
            if s in J:
                count += 1      
        return count 

# Sol 2: two pointers
# Time complexity: O(nlogn); Space complexity: O(m+n)
def numJewelsInStones(self, J, S):
        jewels, stones = [], []
        for j in J:
            jewels.append(j)
        for s in S:
            stones.append(s)
        jewels.sort()
        stones.sort()
        
        pointer1, pointer2 = 0, 0
        count = 0
        while pointer1 < len(jewels) and pointer2 < len(stones):
            if jewels[pointer1] == stones[pointer2]:
                count += 1
                pointer2 += 1
            else:
                if ord(jewels[pointer1]) < ord(stones[pointer2]):
                    pointer1 += 1
                else:
                    pointer2 += 1
        return count 

# Sol 3: bucket count
# Time complexity: O(m+n); Space complexity: O(1)
def numJewelsInStones(self, J, S):
        stones = [0] * 58
        for s in S:
            stones[ord(s)-ord('A')] += 1
        
        count = 0
        for j in J:
            count += stones[ord(j)-ord('A')]
            
        return count 
