# binary search is when we loop through a given data that has been split into two 


def bin_itr(arr, start,end,target):
  while start <= end:

    mid = (start+end)//2

    if arr[mid] < target:
      start = mid + 1

    elif arr[mid] > target:
      end = mid - 1

    else:
      return arr[mid]
  return start


arr = [2,5,8,10,12,18,25]
target = 8

result = bin_itr(arr,0,len(arr)-1,target)

print(result)