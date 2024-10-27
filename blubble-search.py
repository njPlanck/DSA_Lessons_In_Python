def bubble_optimised(A):
  iterations = 0
  for i in range(len(A)):
    for j in range(len(A)-i-1):


      iterations +=1
      if A[j] < A[j+1]:
        A[j],A[j+1] = A[j+1],A[j]
        
  return A,iterations
      
      
           
      
A = [4,7,12,3,6,0,5]

print(bubble_optimised(A))