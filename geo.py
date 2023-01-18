from math import sqrt

# Implementation of a vector
# Basic operations:
#   Adding with another vector
#   Dot product another vector
#   Multiplying a scalar
class Vector:
    def __init__(self, components = [], dimension = -1, constant = 1, label=""):
        self.components = components
        self.constant   = constant
        self.label      = label

        if dimension == -1: self.dimension = len(self.components)
        else:               self.dimension = dimension

    # Traditional dot product WITH ANOTHER VECTOR
    #   Need to be able to dot vector with bivector
    def dot(self, vec):
        if vec.dimension != self.dimension:
            exit()

        return sum([vec.components[c] * self.components[c] for c in range(self.dimension)]) * self.constant**2

    # Generate a Bivector with this vector and another vector
    def wedge(self, ob):
        if type(ob) is Vector:
            return Bivector(self, ob)

    # Basic Length using dot product
    def length(self):
        return sqrt(self.dot(self))

    # Add two VECTORS
    #   Need to be able to add vectors to non-vectors
    def __add__(self, o):
        if o.dimension != self.dimension:
            exit()

        return Vector(
            [self.components[c] * self.constant + o.components[c] * o.constant for c in range(len(self.components))], 
            self.dimension
        )

    # Implementation of dot product/scalar multiplication
    def __rmul__(self, o):
        if type(o) in [int, float]:
            vec = self; vec.constant *= o
            return vec

        elif type(o) is Vector: return self.dot(o)

    def __mul__(self, o):
        if type(o) is float or type(o) is int:
            return o * self 
        
        elif type(o) is Vector: return self.dot(o)

    # Simple "to the power of"
    def __pow__(self, powerof):
        c = self
        for i in range(powerof - 1):
            c = c * c
        return c

    def __getitem__(self, index):
        return self.components[index]

    def __str__(self):
        return "(" + ", ".join([str(c * self.constant) for c in self.components]) + ")"

class Bivector:
    def __init__(self, vec1, vec2, constant = 1):
        self.vec1 = vec1
        self.vec2 = vec2
        self.constant = constant

    def swap(self):
        return Bivector(self.vec1, self.vec2, -1)

    def __mul__(self, o):
        if type(o) in [int, float]:
            return Bivector(self.vec1, self.vec2, self.constant * o)

sigmas = [ Vector([1, 0]), Vector([0, 1]) ]

print(2 * sigmas[0] + 4 * sigmas[1])
