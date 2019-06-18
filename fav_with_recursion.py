lis=[]
def fav(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fav(n-2)+fav(n-1)

print(fav(8))