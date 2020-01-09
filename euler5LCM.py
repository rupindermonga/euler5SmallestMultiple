from functools import reduce

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    return lcm


def get_lcm(a,b):
    return reduce(lambda x, y: lcm(x,y), list(range(a,b+1)))



final = get_lcm(1,20)
print(final)