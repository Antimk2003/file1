from functools import reduce      #import functools

num  = [1,2,3,4,5]
ans = reduce(lambda x , y : x * y , num) 
print(ans)

