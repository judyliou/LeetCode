# Solution 1: dictionary-based
def intersect(self, nums1, nums2):       
    dict1 = {}
    dict2 = {}
    output = []
    for i in nums1:
        dict1[i] = dict1.get(i, 0) + 1
    for i in nums2:
        dict2[i] = dict2.get(i, 0) + 1

    for i in list(dict1.keys()):
        if i in dict2:
            output.extend([i] * min(dict1[i], dict2[i]))
    return output
        
# Solution 2: dictionary-based
def intersect(self, nums1, nums2):
    dict1 = {}
    output = []
    for i in nums1:
        dict1[i] = dict1.get(i, 0) + 1
    for i in nums2:
        if dict1.get(i, 0) > 0:
            output.append(i)
            dict1[i] -= 1  
    return output
        
# Solution 3: pointer-based
def intersect(self, nums1, nums2):
    sort1, sort2 = sorted(nums1), sorted(nums2)

    pt1, pt2 = 0, 0
    output = []
    while pt1 < len(nums1) and pt2 < len(nums2):
        if sort1[pt1] > sort2[pt2]:
            pt2 += 1
        elif sort1[pt1] < sort2[pt2]:
            pt1 += 1
        else:
            output.append(sort1[pt1])
            pt1 += 1
            pt2 += 1
    return output
        
