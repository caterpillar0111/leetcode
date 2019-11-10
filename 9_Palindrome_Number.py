class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        elif x>=0:
            a=[]
            x=str(x)
            for i in range(len(x)):
                a.append(x[i])
            b1=''.join(a)
            a.reverse()
            b2=''.join(a)
            if b1==b2:
                return True
            else:
                return False
