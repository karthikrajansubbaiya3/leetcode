print("hi")

# time complexity of this is o(nlogn)
# because for loop n= number of item it should be o(n) and good sort to be quick sort here we have quick sor is o(n logn)
#o(n)<o(nlogn ) so we can say o(nlogn)
# it is brute force algorithm first we change element into new array and then we square the elements and the sorted 
def sorted_array(array):
    n=len(array)
    res=[0]*n
    for i in range(n):
      res[i]=array[i]**2
    res.sort()
    return res


#print(sorted_array([-4,1,3,5]))
# time complexity of this is o(n)
# because brute force we are traversing array by in timeline integer when go left value is increasing when we go right value is increasing
# so by this square sorted array we can use 0 as right element n-1 as left element it is only for ascending order 
def sorted_squaredarray(array):
   n=len(array)
   i,j=0,len(array)-1
   res=[0]*n
   for k in reversed(range(n)):
      sq_i=array[i]**2
      sq_j=array[j]**2
      if(sq_i>sq_j):
         res[k]=sq_i
         i+=1
      else:
         res[k]=sq_j
         j-=1
   return res
  

      


print(sorted_squaredarray([-5,-4,-2, 1, 9,12]))