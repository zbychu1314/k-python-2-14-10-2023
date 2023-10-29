def generator_12(start=1,is_run = False): 
    while True:
        yield 1
        yield 2
gen = generator_12()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
