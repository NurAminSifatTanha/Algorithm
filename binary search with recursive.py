def binary_recursive(lis, left, right,x):
    if left>right:
        return -1
    mid = (left+ right)//2

    if lis[mid] == x:
        return mid
    if lis[mid] < x:
        return binary_recursive(lis , mid+1 ,right , x)
    else:
        return binary_recursive(lis,left, mid-1,x)

lis=[1,2,3,4,5,6]
for i in range(1,11):
    a = binary_recursive(lis, 0, len(lis) - 1,i)
    if a==-1:
        print("Not Found")
    else:
        print("Found")

# def banary_search(lis,x):
#     left,right = 0, len(lis)-1
#     while left<=right:
#         mid = (left+right)//2
#         if lis[mid]==x:
#             return mid
#         if lis[mid]<x:
#             left = mid+1
#         else:
#             right =mid -1
#
#     return -1
#
#
# a=banary_search([1,2,3,4,5,7 ,8],100)
# if a==-1:
#     print("Not found")
# else:
#     print('Found')
