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
   #visualising recursion:recursion tree,recursion call stack
   #recursion tree 
   # first f(5)=>it calls f(4)=>f(3)=>f(2)=>f(1)=>it returns 1
   #recursion call stack lifo priciple it reurns 1 and then 2 and then 6 and then 24 and then 120
   #iteration vs recursion call stack because of recursion call stack we cannot make ascending or descending phase 
   #iteration does not space complexity it doesnot have recursiv call stack
   #ways to write base condition last valid input or first invalid input
   #recurrence relation 
   #express the solution of a problem as a function of the solutions to smaller instances of the smaller prob;lem
   #recurrence relation-you express the big solution as a combination of smaller ones
   #recursion tree 
   #lets take example of fibonacci series
   #firt we have to have so here f(3)=>f(2) and f(1) alson before calling f(1) and f(2) calls recursively f(0) and f(1) and they return after that f(1) called
   #you can write recursive solution in both ways from o to n and n to o
   #complexity analysis of recursive solution
   #t=>[#nodes]*[work done per node]
   #time complexity of work done at leaf node 
   #ln*w ln+on+won
   #space complexity maximum depth of node is space complexity
   #kth symbol in grammar
   #if 0 becomes '01' 1 becomes 10
   #express the solution of a problem as a function of the solution to smaller instances of the same problem
   #nth row of second half is not of previous row
   #nth row of first half is same as previous row
   # 1<=n<=2n-1
   # k should not be greater than previous condition
   #if k<half return(n-1,k)
   #if k>half return(n-1,k-mid)
# for k greater thamn mid would be flipped value
def Kth_symbol(n,k):
     len=2**(n-1)
     mid=len//2
     if n==1: return 0
     if k<=mid:
        return Kth_symbol(n-1,k)
     else:
        return 1- Kth_symbol(n-1,k-mid)
     
print(Kth_symbol(3,0))
     
   #when you have something circular consider %(modulo)=>remainder after divison
# something is circular we should have to use modulus 
#for example k=7 modulus of len(arr) k=7 (0+7-1)%4=6%4=2 like wise it goes untill reach the base condition
# why we use index to remove should be as start index because we remove the element from array we have to start from 
# we have to start next to element of removed element
# it works in case for index of 4 for 4 element array so k=4 the element 3 has to removed next loop starts with 3 instead of 0
#but it works (3+4-1)%3=0 element the next to removed worked well
def findTheWinner(n,k):
   arr=[i+1 for i in range(n)]

   def helper(arr,start_index):
      if len(arr)==1:
         return arr[0]
      index_to_remove=(start_index+k-1)%len(arr)
      del arr[index_to_remove]
      return helper(arr,index_to_remove)
   return helper(arr,0)
#here k-1 because index starts 0
#jospheus problem circular four people k will be position to be elimanted after that eliminated behind will be started 
#if it start of same index also works


   
def winner(n,k):
   arr=[i+1 for i in range(n)]

   def jospeus(n):
      if n==1:
         return 0
      return(jospeus(n-1)+k)%n
   
   return jospeus(n)+1
#it is recursive approach here 
   
#solving sub problem of n-1 we can have the result of n 
# 0 indexed approach so we can have that add 1 at last
#iterative approach
def winneriterative(n,k):
   arr=[i+1 for i in range(n)]
   survivor=0    
   for i in range(2,n+1):
     survivor=(survivor+k) % i
   return survivor+1
#the flow of iterative approach is n=1 it will return 0 and then n=2 (0+k)%2=1 then we need add result to survivor
# like this it is going
#can solving subproblem help to solve the problem


def towerofhanoi(n,fromrod,torod,auxrod):
   count=0
   def helper(n,fromrod,torod,auxrod):
      nonlocal count
      #base case
      if n==1:
         print("move disk" + str(n) + "from rod" +str(fromrod)+"   to rod" +str(torod))
         count+=1
         return
      helper(n-1,fromrod ,auxrod,torod)
      print("move disk" + str(n) + "from rod" +str(fromrod)+"    to rod" +str(torod))
      count+=1
      helper(n-1,auxrod,torod,fromrod)
   helper(n,fromrod,torod,auxrod)
   return count

print(towerofhanoi(3,'a','b','c'))
#time complexity of is this o(2^n) we are moving n-1 disk two times n disk one time 
# and also recursive call stack o(n) should be space complexity
#power sum problem
# for example [1,2,3,4] the array would be like power would be 1
# for example [1,2,[3,4],[[2]]] for (3+4)^2 number of nested level sum of power
# time complexity would be 0(n) for the above one is 8
# time complexity is sum of elements  in array as well as sub array if it is presen or not that would be count

def powersum(array,power=1):
   sum=0
   n=len(array)
   for i in array:
      if type(i)==list:
         sum+=powersum(i,power+1)
      else:
         sum+=i
   return sum**power


print(powersum([1,2,[3,4],[[2]]]))
# back tracking
# is algorithmic approach to find solutions to problems that involve many possible path
# solution are built by step by step recursion
# if a path does not leads to a solution /violates constraint
# make changes in place (pass by reference)
# modified the state of the problem in place instead of copied
# how it is different from recursion
# controlled recursion + modify state of the problem in place (pass by reference)
# how does the backtracking works
# explore one option
# keep building the solution with recursion
# violates coditio->backtrack,explore new path
# brute force generate all possible solution validate the condition it satifies given criteria
# permutation of abc should be sove in two ways one way is by creating new array each time making new 
# instead of going in one by one swaping in place bca like we are not creating new memory 
# identify when to use recursion 
# if a problem requires every possible path 
# there are multiple solution and you want all of them
# not for optimization find the largest,smallest,greatest
# permutation
# question:given an array nums of distint integers,return all the possible permutation,you can return
# the answer in any order
# backtracking for example 1,2,3 permutation
# for this -,-,- three position 1st position has three posibilities 3
# for 2nd position has two posibilites 2
# for 3rd position has one posiblity 1
# total num of comination is 3! =3*2*1
# for pseudocode problem
#swap of j to range(index,n) and swap if it reaches base conditon make copy of it 
# again swap this is backtracking from the previous position we are able to make new combination

def permute(nums):
   n=len(nums)
   res=[]
   def helper(index):
      if index==n-1:
        res.append(nums[:])
        return 
      for j in range(index,n):
         nums[index],nums[j]=nums[j],nums[index]
         helper(index+1)
         nums[index],nums[j]=nums[j],nums[index]
   helper(0)
   return res


