#permutation is the process of getting different vvariations of a given set of unique data

#swapping two letters

'''
def perm(string, pocket=""):

  length = len(string)
  if length == 0:
    return pocket
  
  else:
    for i in range(length):
      letter = string[i]
      front = string[0:i]
      back = string[i+1:]
      together = front + back
      perm(together, letter + pocket)

print(perm("ern",""))

'''

def perm(string,pocket=""):
  if len(string)==0:
    print(pocket)
  else:
    for i in range(len(string)):
      letter = string[i]
      front = string[0:i]
      back = string[i+1:]
      together = front + back
      perm(together,letter + pocket)




print(perm("ABC",""))