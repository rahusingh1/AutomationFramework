import inspect

def whoami():
    return inspect.stack()[1][3]


def Myfun():
    x = whoami()
    print(x)

Myfun()