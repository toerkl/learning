#!/usr/bin/env python


def toggle(status):
    x = [1, 0]
    toggle = x[status]
    return toggle

status = 1

status = toggle(status)
print(status)

status = toggle(status)
print(status)



