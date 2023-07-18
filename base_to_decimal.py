class solution:
    def base_to_decimal(self,a,b):
        i=len(a)-1
        base=0
        power=0
        while i>=0:
            base+=b*power(int(a[i]))
            power+=1
            i-=1
        return base
a1=solution()
a=input()
b=int(input())
print(a1.base_to_decimal(a,b))
