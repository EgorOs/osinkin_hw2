#!/usr/bin/env python3
from inspect import signature, Parameter


def partial(func, *fixated_args, **fixated_kwargs):
    def wrapper(*args, **kwargs):
        new_kwargs = kwargs.copy()
        new_kwargs.update(fixated_kwargs)
        return func(*(fixated_args + args), **new_kwargs)

    try:
        #  If possible acquire names for positional arguments
        sig = signature(func)
        arg_names = [name for name in sig.parameters.keys()]
        named_fixated_args = dict(zip(arg_names[:len(fixated_args)], fixated_args))
    except Exception as e:
        #  For built-in functions such as round and range
        print('WARNING: ' + str(e))
        named_fixated_args = fixated_args

    wrapper.__name__ = 'partial_' + func.__name__
    wrapper.__doc__ = """ A partial implementation of {}
    with pre-applied arguments being:
    {}  {} """.format(
        func.__name__, named_fixated_args, fixated_kwargs)
    return wrapper


#  Check
def f(a, b, c=1):
    return sum([a,b,c])


f = partial(f, 10, c=100)
print(f.__doc__)
print(f(1))

round = partial(round, 1.234, ndigits=1)
print(round.__doc__)
print(round())