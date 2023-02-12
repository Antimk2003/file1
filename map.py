def pow(n):
    return n**n
number = [1,2,4,3,9,7,5]
result = map(pow,number)
print(list(result))


def myfuc(n):
    return len(n)

x = map(myfuc, ("apple","banana"))
print(x)
print(tuple(x))