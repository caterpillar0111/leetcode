class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        if strs ==[]:
            return ""
        else:
            key=strs[0]
            for i in range(len(key)):
                for string in (strs[1:]):
                    if (key[i]!=string[i])or(i>len(string)):
                        return key[:i]
        return  key
            
