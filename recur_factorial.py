def recur_factorial(n):
  if n == 1:
    return n
  else:
    temp = recur_factorial(n-1)
    temp *=n

    return temp



n = 5

print(recur_factorial(n))