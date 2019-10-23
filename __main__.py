from lab_python_oop.rectangle import Rect
from lab_python_oop.square import Square
from lab_python_oop.circle import Circle


def main():
    r = Rect(3, 2, "blue")
    c = Circle(5, "green")
    s = Square(5, "red")
    print(r.repr())
    print(c.repr())
    print(s.repr())


if __name__ == "__main__":
    main()
