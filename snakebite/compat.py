from sys import version_info
py_2 = version_info[0] < 3

long = py_2 and (long) or (int)
range = py_2 and (xrange) or (range)
unicode = py_2 and (unicode) or (str)
