#!/usr/bin/env python3

ctr = 0

def make_it_count(func, counter_name):
    def wrapper(*args, **kwargs):
        globals()[counter_name] += 1
        return func(*args, **kwargs)
    return wrapper

m = make_it_count(sum, 'ctr')
for i in range(10):
    m([1,2,3])

print(ctr)