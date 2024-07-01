class Solution:

    @cache
    def solve(self , i ,prev , ip) :

        if i >= len(self.s) :
            if ip.count(".") == 3 :
                l = list(map(str , ip.split(".")))

                lis = [1 if ( x!="" and  (x[0]!="0" or x=="0") and int(x)>=0 and int(x)<=255 ) else 0 for x in l ]
                if sum(lis) == 4 :
                    self.ans += [ip]
            return 

        self.solve(i+1 , prev + self.s[i] , ip + self.s[i])
        if i<len(self.s):
            self.solve(i+1 , self.s[i] , ip + self.s[i] + ".")

        return 


    def restoreIpAddresses(self, s: str) -> List[str]: 
        self.s = s 
        self.ans = []
        self.solve(0,"","")
        return self.ans
        