def lengthOfLongestSubstring(self, s):
    left = 0
    setn=set()
    length=0
    for right in range(len(s)):
        while s[right] in setn:
            setn.remove(s[left])
            left+=1
        setn.add(s[right])
        length=max(length,right-left+1)
    return length