#!/usr/bin/env python3


def partial(func, *fixated_args, **fixated_kwargs):
    def wrapper(*args, **kwargs):
        new_kwargs = kwargs.copy()
        new_kwargs.update(fixated_kwargs)
        return func(*(fixated_args + args), **new_kwargs)

    wrapper.__name__ = 'partial_' + func.__name__
    wrapper.__doc__ = """ A partial implementation of {}
    with pre-applied arguments being:
    {}  {} """.format(
        func.__name__, fixated_args, fixated_kwargs)
    return wrapper
