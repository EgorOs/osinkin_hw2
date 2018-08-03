#!/usr/bin/env python3


def letters_range(*args):

    if len(args) > 3:
        raise TypeError('letters_range expected at most 3 arguments, got {}'.format(len(args)))
    elif len(args) < 3:
        for i, arg in enumerate(args):
            if not isinstance(arg, str):
                raise TypeError('str argument expected, not {}'.format(type(args[i]).__name__))

    ltr = []

    # Replace letters with their indices
    args_to_num = [ord(arg.lower()) if isinstance(arg, str) else arg for arg in args]

    if len(args_to_num) == 1:
        args_to_num = [ord('a')] + args_to_num

    for i in range(*args_to_num):
        ltr.append(chr(i))
    return ltr

print(letters_range('A','k', 2))

# bad cases (1), ('a',1), ('a','l','m',1)
# import string ??? # shorter if dict is used
# if not in ascii.lowercase() --> invalid character
# do I need out of bounds check