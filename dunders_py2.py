"""
Conclusions:

1. `print(o)` equals to `print(str(o))`
2. `str(o)` will use `__repr__` if `__str__` not exist
3. `repr(o)` only uses `__repr__`
4. `unicode(o)` will use `unicode(__str__())` if `__unicode__` not exist
"""


class A(object):
    dunder_methods = ['__str__']

    def __str__(self):
        return 'a __str__'


class B(object):
    dunder_methods = ['__unicode__']

    def __unicode__(self):
        return u'b __unicode__'


class C(object):
    dunder_methods = ['__repr__']

    def __repr__(self):
        return 'c __repr__'


class D(object):
    dunder_methods = ['__str__', '__unicode__']

    def __str__(self):
        return 'd __str__'

    def __unicode__(self):
        return u'd __unicode__'


class E(object):
    dunder_methods = ['__str__', '__repr__']

    def __str__(self):
        return 'e __str__'

    def __repr__(self):
        return 'e __repr__'


class F(object):
    dunder_methods = ['__unicode__', '__repr__']

    def __unicode__(self):
        return u'f __unicode__'

    def __repr__(self):
        return 'f __repr__'


class G(object):
    dunder_methods = []


def prints(o):
    print('{} with {}'.format(
        o.__class__.__name__,
        ' '.join(o.dunder_methods),
    ))
    print '  print:',
    print(o)
    print('  str: {!s}'.format(o))
    print('  repr: {!r}'.format(o))
    try:
        print('  unicode: {!r}'.format(unicode(o)))
    except Exception as e:
        print('  unicode: {}, {}'.format(e.__class__.__name__, e))
    print


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
