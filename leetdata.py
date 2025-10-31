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
#if it is monotonic decreasing from left to right or monotonic increasing from left to right
#space complexity is o(1) no extra space used
print("monotonic array")
def monotonic_array(array):
   n=len(array)
   if n==0:
      return True
   first=array[0]
   last=array[n-1]
   if first>last:
      #md or it is no monotonic
      for k in range(n-1):
         if array[k]<array[k+1]:
            return False
         elif first==last:
            for k in range(n-1):
               if array[k]!=array[k+1]:
                  return False
   else:
      #first<last
      for k in range(n-1):
         if array[k]>array[k+1]:
            return False
   return True
print(monotonic_array([1,2,2,3]))
print(monotonic_array([9,8,7,6,5,5,5,5,4,3,2,1]))