def binary_search(l,key):
  low=0
  high=len(l)-1
  found=False
  while low<=high and not found:
    mid=(low+high)//2
    if key==l[mid]:
      found=True
    elif key<l[mid]:
      high=mid-1
    else:
      low=mid+1
  if found==True:
    print("Key is found")
  else:
    print("Key is not found")
    
l=list(map(int,input().split()))
l.sort()
key=int(input())
binary_search(l,key)
