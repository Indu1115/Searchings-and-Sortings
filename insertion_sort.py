def insertion_sort(l):
  for i in range(1,len(l)):
    pos=i
    curr_ele=l[i]
    while curr_ele<l[pos-1] and pos>0:
      l[pos]=l[pos-1]
      pos=pos-1
    l[pos]=curr_ele
    
l=list(map(int,input().split()))
insertion_sort(l)
print(l)
