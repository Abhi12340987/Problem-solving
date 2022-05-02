def area(a, b):
    return a * b

print(area(4, 5))

def mean(*args):
    return sum(args) / len(args)
print(mean(1, 2, 3, 4, 5))



def mean(**kwargs):
    return kwargs

print(mean(a = 1, b=2, c=3))