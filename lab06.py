class Lab06:

    def solve01(self,grades_data):
        a,l=[],[]
        for i in grades_data:
            a=grades_data[i]
            s=sum(a)
            l.append((i,s))
        def get_sec(t):
            return t[1]
        l.sort(key=get_sec, reverse=True)
        return l
        

    def solve02(self,elections):
        pass

    def solve03(self,message):
        pass

    def solve04(self,L):
        pass

    def solve05(self,A,B):
        pass

    def solve06(self,synonyms,query):
        pass

    def solve07(self,A,B):
        pass

    def solve08(self,n,x,y):
        pass

#Write your tests below.
# soln = Lab06()
# print(soln.solve01({57:[25,23,35],12:[10,10,20],50:[45,48,50]}))