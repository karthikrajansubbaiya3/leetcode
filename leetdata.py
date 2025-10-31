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
# function calling itself untill base condition /terminating condition occurs
#making the input close to base condition or the terminating condition
# space complexity is o(n) because each function call is stored in call stack 
# base condition is important to avoid infinite recursion
# when to use recursion
# when problem can be broken into sub problem
# solve the sub problem and use these solution to construct solution to original problem
# when we need to explore all possible solution
# when we need to traverse a tree or graph
# when we need to backtrack
# when we need to implement divide and conquer algorithm
# when we need to implement dynamic programming algorithm
# when we need to work with recursive data structure like linked list and tree
# when we need to simplify complex problem
def factorial(n):
   # base condition
   if n==0 or n==1:
      return 1
   else:
      return n*factorial(n-1)
print(factorial(5))
# fibonacci series using recursion
def fibonacci(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(5))  
# find gcd using recursion
def gcd(a,b):
   if b==0:
      return a
   else:
      return gcd(b,a%b)
print(gcd(48,18))  
# find power of a number using recursion
def power(x,n):
   if n==0:
      return 1
   else:
      return x*power(x,n-1)
print(power(2,3))
# find sum of digits using recursion
def sum_of_digits(n):
   if n==0:
      return 0
   else:
      return n%10+sum_of_digits(n//10)
print(sum_of_digits(1234))
# find reverse of a string using recursion
def reverse_string(s):
   if len(s)==0:
      return s
   else:
      return s[-1]+reverse_string(s[:-1])
print(reverse_string("hello"))
# find maximum element in an array using recursion
def max_in_array(array,n):
   if n==1:
      return array[0]
   else:
      return max(array[n-1],max_in_array(array,n-1))
print(max_in_array([1,5,3,9,2],5))
# find minimum element in an array using recursion
def min_in_array(array,n):
   if n==1:
      return array[0]
   else:
      return min(array[n-1],min_in_array(array,n-1))
print(min_in_array([1,5,3,9,2],5))
# find length of a string using recursion
def length_of_string(s):
   if s=="":
      return 0
   else:
      return 1+length_of_string(s[1:])
   #how to use recursion to solve problems
   # understand the problem
   #identify the sub problems
   #trust/faith
   #link 1 and link2
   # base condition
   