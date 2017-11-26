import collections

Point3D = collections.namedtuple('Point3D', ['x','y','z'])
p = Point3D(x=1.0, y=0.7, z=0.0)

print(p)
# Point3D(x=1.0, y=0.7, z=0.0)
print('p.x:', p.x)
# p.x: 1.0
print('p.y:', p.y)
print('p.z:', p.z)