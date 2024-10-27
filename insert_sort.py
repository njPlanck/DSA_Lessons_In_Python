def insert_sort(A):
   for j in range(1,len(A)):
     key = A[j]
     i = j-1
     while i >=0 and A[i]<key:
       A[i+1] = A[i]
       i-=1
       A[i+1] = key
   return A
       


A = [4,7,12,3,6,0,5]

print(insert_sort(A))