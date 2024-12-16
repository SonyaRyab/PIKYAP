import sys
import math
import abc
from lab_python_oop.Circle import Circle
from lab_python_oop.FigColor import FigColor
from lab_python_oop.GeomFig import Figure
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square

def main():
    N = 15
    c = Circle(N)
    print(c.area())
    print("Прямоугольник синего цвета шириной ", N, "и высотой ", N)
    print("Круг зеленого цвета радиусом ", N)
    print("Квадрат красного цвета со стороной ", N)


if __name__ == "__main__":
    main()
