from functools import wraps
import time
def bold(f):
    @wraps(bold)
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        r =f"<b>{r}<b>"
        return r
    return wrapper

@bold
def zlacz_teksty(*args, sep="\n"):
    return "\n".join(args)

def italic(f):
    @wraps(italic)
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        r =f"<i>{r}<i>"
        return r
    return wrapper  


print(zlacz_teksty("A", "B"))

@italic
def zlacz_teksty(*args, sep="\n"):
    return "\n".join(args)

print(zlacz_teksty("A", "B"))

def timreit(f):
    @wraps(italic)
    def wrapper(*args, **kwargs):
        t = time.time()
        print(f'Start funkcji:')
        r = f(*args, **kwargs)
        print(f'Wykonanie zajelo: {time.time()-t} s')
        return r
    return wrapper 

@timreit
def zlacz_teksty(*args, sep="\n"):
    return "\n".join(args) 

print(zlacz_teksty("A", "B"))

