class Solution(object):
    def reverse(self, x):
        a=[]
        if x>0:
            x=str(x)
            for j in range(len(x)):
                a.append(x[j])
            a.reverse()
            b=''.join(a)
            b=abs(int(b))
            if b>pow(2,31):
                b=0
        elif x==0:
            b=0
        elif x<0:
            x=-x
            x=str(x)
            for i in range(len(x)):
                a.append(x[i])
            a.reverse()
            b=''.join(a)
            b=abs(int(b))
            if b>pow(2,31):
                b=0
            else:
                b=-b

        return b
    
        """
        :type x: int
        :rtype: int
        """
