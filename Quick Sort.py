def quickSort(array,start,ends):
   if start>=ends:
       return
   part=Partition(array,start,ends)
   quickSort(array,start,part-1)
   quickSort(array,part+1,ends)

def Partition(array,start,ends):
   pivot=array[ends]
   index=start
   for i in range(start,len(array)-1):
       if array[i]<=pivot:
           array[index],array[i]=array[i],array[index]
           index+=1
   array[index],array[ends]=array[ends],array[index]
   return index

array=[int(x) for x in input().split()]
quickSort(array,0,len(array)-1)
print(array)

