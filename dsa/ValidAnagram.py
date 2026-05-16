class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        found = True
        if len(s) == len(t):
            for ch in s:
                if ch not in t:
                    found = False
                    break
                else:
                    t =t.replace(ch,"",1)
        else:
            found = False
        return found