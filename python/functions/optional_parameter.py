#!/usr/bin/env python3


def currency(n, w=15):
    """ Show in currency format, width 15
    or whatever you set it to """
    s = f"${n:,.2f}"
    return s.rjust(w)


print(currency(100, w=20))
