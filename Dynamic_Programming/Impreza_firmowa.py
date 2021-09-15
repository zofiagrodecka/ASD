class Employee:
    def __init__(self, fun, name):
        self.emp = []
        self.fun = fun
        self.name = name
        self.presence = False
        self.f = -1
        self.g = -1


def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for vi in v.emp:
        x += g(vi)
    y = g(v)
    v.f = max(x,y)
    if v.f == x:
        v.presence = True
    return v.f


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for vi in v.emp:
        v.g += f(vi)
    return v.g


def attendance(root):
    if root is None:
        return
    if root.presence == True:
        print(root.name)
    for i in root.emp:
        attendance(i)
