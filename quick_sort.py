def pivot_place(l,start,end):
  pivot=l[start]
  left=start+1
  right=end
  while True:
    while left<=right and l[left]<=pivot:
      left+=1
    while left<=right and l[right]>=pivot:
      right-=1
    if right<left:
      break
    else:
      l[left],l[right]=l[right],l[left]
  l[start],l[right]=l[right],l[start]
  return right

def quick_sort(l,start,end):
  if start<end:
    p=pivot_place(l,start,end)
    quick_sort(l,start,p-1)
    quick_sort(l,p+1,end)
    
l=list(map(int,input().split()))
quick_sort(l,0,len(l)-1)
print(l)
