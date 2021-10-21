def linear_search(l,key):
 for i in range(len(l)):
 if(l[i]==key):
 return i
 return -1
l=list(map(int,input().split()))
key=int(input())
result=linear_search(l,key)
if(result==-1):
 print(key,"is not found")
else:
 print(key,"is found at",result)
