ages = [5,12,17,18,24,32]
def myfunc(ages):
    if ages < 18:
        return False 
    else:
        return True
adults = filter(myfunc,ages) 

for ages in adults :
    print(ages)