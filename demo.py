from py_enum import Enum

if __name__ == "__main__":
    COLOR = Enum("RED", "BLUE", "GREEN")
    SHAPES = Enum(SQUARE=5, RECTANGLE=6, CIRCLE=9)
    FRUITS = Enum("ORANGE", "BANANA", MANGO=2, LEMON=0)

    print(COLOR)
    print(SHAPES)
    print(FRUITS)
    # get val using .
    print(f"{COLOR.RED=}")
    assert COLOR.RED == 0
    print(f"{SHAPES.SQUARE = }")
    assert SHAPES.SQUARE == 5
    print(f"{FRUITS.ORANGE = }")
    assert FRUITS.ORANGE == 3
    print(f"{FRUITS.MANGO  = }")
    assert FRUITS.MANGO == 2
    print(f"{FRUITS.LEMON  = }")
    assert FRUITS.LEMON == 0

    for i in FRUITS:
        print(i)
