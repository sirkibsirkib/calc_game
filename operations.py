
class Operation:
    def __init__(self, printable, func):
        self.printable = printable;
        self.func = func

    def apply_to(self, x):
        return self.func(x)

    def __repr__(self):
        return self.printable



def o_add(x):
    printable = '+' + str(x)
    func = lambda q : q+x
    return Operation(printable, func)

def o_sub(x):
    printable = '-' + str(x)
    func = lambda q : q-x
    return Operation(printable, func)

def o_mult(x):
    printable = '*' + str(x)
    func = lambda q : q*x
    return Operation(printable, func)

def o_div(x):
    printable = '/' + str(x)
    func = lambda q : q/x
    return Operation(printable, func)

def o_insert(x):
    printable = '_' + str(x)
    func = lambda q : q if q==0 else int(str(q) + str(x))
    return Operation(printable, func)


def map_digit(input, old, new):
    return int(
        ''.join(str(input).replace(str(old), str(new)))
    )


def o_map(x, y):
    printable = str(x) + '=>' + str(y)
    func = lambda q : map_digit(q, x, y)
    return Operation(printable, func)

o_flip = Operation('+-', lambda x : -x)
o_del = Operation('<<', lambda x : int(x/10))
