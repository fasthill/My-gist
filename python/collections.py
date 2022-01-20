import collections

# namedTuple

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
print(p[0] + p[1])

x, y = p
print(x, y)

psum = p.x + p.y
print(psum)

print(p)

p.y = 40  # generate error! can't change its value.
