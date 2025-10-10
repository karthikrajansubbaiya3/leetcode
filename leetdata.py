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


print(sorted_array([-4,1,3,5]))