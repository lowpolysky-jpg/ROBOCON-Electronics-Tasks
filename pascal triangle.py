class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        l=[[1]]
        for bl in range(1, numRows):
            lastl=l[-1]
            newl = [1]
            for i in range (len(lastl)-1):
                newl.append(lastl[i]+lastl[i+1])
            newl.append(1)
            l.append(newl)
        return l