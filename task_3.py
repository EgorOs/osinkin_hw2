#!/usr/bin/env python3


def atom(value=None):
    def get_value():
        nonlocal value
        return value

    def set_value(new_value):
        nonlocal value
        value = new_value
        return value

    def process_value(*funcs):
        nonlocal value
        for f in funcs:
            value = f(value)
        return value
    return get_value, set_value, process_value


#  Check
def sqr(v):
    return v*v


get_value, set_value, process_value = atom()
print(get_value())
set_value(11)
print(get_value())
print(process_value(sqr,sqr,range,len))