"""
Conclusions:

1. `print(o)` equals to `print(str(o))`
2. `str(o)` will use `__repr__` if `__str__` not exist
3. `repr(o)` only uses `__repr__`
4. `bytes(o)` only uses `__bytes__`
"""


class A:
    dunder_methods = ['__str__']

    def __str__(self):
        return 'a __str__'


class B:
    dunder_methods = ['__bytes__']

    def __bytes__(self):
        return b'b __bytes__'


class C:
    dunder_methods = ['__repr__']

    def __repr__(self):
        return 'c __repr__'


class D:
    dunder_methods = ['__str__', '__bytes__']

    def __str__(self):
        return 'd __str__'

    def __bytes__(self):
        return b'd __bytes__'


class E:
    dunder_methods = ['__str__', '__repr__']

    def __str__(self):
        return 'e __str__'

    def __repr__(self):
        return 'e __repr__'


class F:
    dunder_methods = ['__bytes__', '__repr__']

    def __bytes__(self):
        return b'f __bytes__'

    def __repr__(self):
        return 'f __repr__'


class G:
    dunder_methods = []


def prints(o):
    print('{} with {}'.format(
        o.__class__.__name__,
        ' '.join(o.dunder_methods),
    ))
    print('  print: ', end='')
    print(o)
    print('  str: {!s}'.format(o))
    print('  repr: {!r}'.format(o))
    try:
        print('  bytes: {!r}'.format(bytes(o)))
    except Exception as e:
        print('  bytes: {}, {}'.format(e.__class__.__name__, e))
    print()


if __name__ == '__main__':
    a = A()
    prints(a)

    b = B()
    prints(b)

    c = C()
    prints(c)

    d = D()
    prints(d)

    e = E()
    prints(e)

    f = F()
    prints(f)

    g = G()
    prints(g)
