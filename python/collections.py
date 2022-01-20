import collections

# namedTuple
# https://realpython.com/python-namedtuple/

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
print(p[0] + p[1])

x, y = p
print(x, y)

psum = p.x + p.y
print(psum)

print(p)

p.y = 40  # generate error! can't change its value.

Person = collections.namedtuple("Person", "name children")
john = Person("John Doe", ["Timmy", "Jimmy"]) # the Person -name-d 'John Doe' has two -chidren- 'Timmuy and Jimmy'

print(john)

print(john.children)

john.children.append('Tina')
# You can create named tuples that contain mutable objects. You can modify the mutable objects in the underlying tuple. 
print(john.children)
