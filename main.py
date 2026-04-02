import math
class Figure:
    def perimeter(self):
        return 0
    def square(self):
        return 0
    def volume(self):
        return 0
    
class Circle(Figure):
    def __init__(self, r):
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def square(self):
        return math.pi * self.r ** 2

class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.b

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
    def square(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        p = self.perimeter() / 2
        return math.sqrt(max(p*(p-self.a)*(p-self.b)*(p-self.c), 0))

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def perimeter(self):
        return 2 * (self.a + self.b)
    def square(self):
        return self.a * self.h

class Trapeze(Figure):
    def __init__(self, a, b, c, d, h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    def square(self):
        return (self.a + self.b) / 2 * self.h

class RectangularParallelepiped(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    def square(self):
        return 2 * (self.a*self.b + self.a*self.h + self.b*self.h)
    def volume(self):
        return self.a * self.b * self.h

class Cone(Figure):
    def __init__(self, r, h):
        self.r = r
        self.h = h
    def square(self):
        l = math.sqrt(self.r**2 + self.h**2)
        return math.pi * self.r * (self.r + l)
    def volume(self):
        return (1/3) * math.pi * self.r**2 * self.h

class Ball(Figure):
    def __init__(self, r):
        self.r = r
    def square(self):
        return 4 * math.pi * self.r**2
    def volume(self):
        return (4/3) * math.pi * self.r**3

class TriangularPyramid(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def square(self):
        return self.a * self.a
    def volume(self):
        return (1/3) * self.a**2 * self.h

class QuadrangularPyramid(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h
    def square(self):
        return self.a * self.a
    def volume(self):
        return (1/3) * self.a**2 * self.h

class TriangularPrism(Figure):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def square(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(max(p*(p-self.a)*(p-self.b)*(p-self.c), 0))
    def volume(self):
        p = (self.a + self.b + self.c) / 2
        base = math.sqrt(max(p*(p-self.a)*(p-self.b)*(p-self.c), 0))
        return base * self.h

figures = []
for i in range(1, 4):
    file = f"input0{i}.txt"
    with open(file) as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            name = parts[0]
            try:
                if name == "Circle":
                    figures.append(Circle(float(parts[1])))
                elif name == "Rectangle":
                    figures.append(Rectangle(float(parts[1]), float(parts[2])))
                elif name == "Triangle":
                    figures.append(Triangle(float(parts[1]), float(parts[2]), float(parts[3])))
                elif name == "Parallelogram":
                    figures.append(Parallelogram(float(parts[1]), float(parts[2]), float(parts[3])))
                elif name == "Trapeze":
                    figures.append(Trapeze(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])))
                elif name == "RectangularParallelepiped":
                    figures.append(RectangularParallelepiped(float(parts[1]), float(parts[2]), float(parts[3])))
                elif name == "Cone":
                    figures.append(Cone(float(parts[1]), float(parts[2])))
                elif name == "Ball":
                    figures.append(Ball(float(parts[1])))
                elif name == "TriangularPyramid":
                    figures.append(TriangularPyramid(float(parts[1]), float(parts[2])))
                elif name == "QuadrangularPyramid":
                    figures.append(QuadrangularPyramid(float(parts[1]), float(parts[2])))
                elif name == "TriangularPrism":
                    figures.append(TriangularPrism(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))
            except:
                continue

max_area = 0
max_type = ""
for fig in figures:
    area = fig.square()
    if area > max_area:
        max_area = area
        max_type = type(fig).__name__

with open("output.txt", "w") as f:
    f.write(f"Max area: {max_area}\n")
    f.write(f"Figure type: {max_type}")

print("Done. Check output.txt")
