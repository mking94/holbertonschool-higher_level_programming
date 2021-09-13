#!/usr/bin/python3
# 3-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
  """Print in reverse."""
  if my_list is None:
    return (None)
  i = len(my_list) - 1
  while i >= 0:
    print("{:d}".format(my_list[i]))
    i -= 1
