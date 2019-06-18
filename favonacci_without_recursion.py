lis=[0,1]
def fav(n):
    if n==0:
        return 0
    else:
        a,b=0,1
        for i in range(1,n):
            a,b=b,a+b
            lis.append(b)
        return lis

for key , value in enumerate(fav(8)):
    print(key,value)