import matplotlib.pyplot as plt
from pprint import pprint
import inspect


def introspection_info(plt):
    pass

print(type(introspection_info))
print()
print(callable(introspection_info))
print()
print(type(plt))
print()
print(getattr(plt, 'matplotlib', 'нет?'))
print()
# pprint(dir(plt))

# print(help(plt))

# pprint(inspect.getsource(plt))

print(inspect.getfullargspec(introspection_info))
print()
for x in dir(plt):
    y = getattr(plt, x)
    print(x,type(y))

