#!/usr/bin/env python3

from string import ascii_lowercase


def letters_range(*args):

    if len(args) > 3:
        raise TypeError(
            'letters_range expected at most 3 arguments, got {}'
            .format(len(args)))

    elif len(args) <= 3:
        if len(args) == 3 and not isinstance(args[2], int):
            raise TypeError('step must be an int, got {}'
                            .format(type(args[2]).__name__))
        for arg in args[:2]:
            if str(arg) not in ascii_lowercase:
                raise TypeError('ascii_lowercase character expected, got {}'
                                .format(arg))

    ltr = []

    # Replace letters with their indices
    args_to_num = [ord(arg.lower()) if isinstance(arg, str) else arg for arg in args]

    if len(args_to_num) == 1:
        args_to_num = [ord('a')] + args_to_num

    for i in range(*args_to_num):
        ltr.append(chr(i))
    return ltr
