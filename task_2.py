#!/usr/bin/env python3

ctr = 0


def make_it_count(func, counter_name):
    def wrapper(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)
    return wrapper


# Check
counted_len = make_it_count(len, 'ctr')
for i in range(10):
    counted_len('abcd')
print(ctr)
