def bubble_sort(l):
  for i in range(len(l)-1):
    for j in range(len(l)-1):
      if l[j]>l[j+1]:
        l[j],l[j+1]=l[j+1],l[j]
     
l=list(map(int,input().split()))
bubble_sort(l)
print(l)
