def iterative_factorial(n):
  fact = 1
  for i in range(2,n+1):
    fact *= i
    print(i)
    print(fact)


n=8
print(iterative_factorial(n))