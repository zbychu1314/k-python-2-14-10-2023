def power_factory(i=1):
    while i <10:
        yield lambda x:x**i
        i += 1


f = power_factory()
z =2
for i in range(3):
    z = next(f)(z)
    print("z", z)