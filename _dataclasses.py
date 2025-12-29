from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

point = Point(1,2)
print(point.x, point.y)