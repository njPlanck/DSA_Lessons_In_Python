# this program calculates the factorials of numbers with recursion

#Recusrsion is when a function calls itself


# using the for loop
'''
def fact(n):
  num = 1
  for i in range(2,n+1):
    num *= i
  return num





print(fact(5))

'''

#using recursion


def fact(n):
  if(n==1 or n == 0):
    return 1
  else:
    temp = fact(n-1)
    return temp * n



print(fact(5))