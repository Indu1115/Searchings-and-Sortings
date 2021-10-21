def selection_sort(l):
  for i in range(len(l)):
    min_val=min(l[i:])
    min_index=l.index(min_val)
    l[i],l[min_index]=l[min_index],l[i]
  
l=list(map(int,input().split()))
selection_sort(l)
print(l)
