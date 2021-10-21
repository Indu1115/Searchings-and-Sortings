def merge_sort(l):
  if len(l)>1:
    mid=len(l)//2
    left_list=l[:mid]
    right_list=l[mid:]
    merge_sort(left_list)
    merge_sort(right_list)
    i,j,k=0,0,0
    while i<len(left_list) and j<len(right_list):
      if left_list[i]<right_list[j]:
        l[k]=left_list[i]
        i=i+1
        k=k+1
      else:
        l[k]=right_list[j]
        j=j+1
        k=k+1
    while i<len(left_list):
      l[k]=left_list[i]
      i=i+1
      k=k+1
    while j<len(right_list):
      l[k]=right_list[j]
      j=j+1
      k=k+1
  
l=list(map(int,input().split()))
merge_sort(l)
print(l)
