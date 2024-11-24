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

    # GET VALUE BY CALLING
    print(f"{SHAPES('SQUARE') = }")
    print(f"{FRUITS(3)        = }")
    print(f"{FRUITS('MANGO')  = }")
    print(f"{FRUITS(0)        = }")

    # GET VALUE BY INDEX
    print(f"{SHAPES['SQUARE'] = }")
    print(f"{FRUITS[3]        = }")
    print(f"{FRUITS['MANGO']  = }")
    print(f"{FRUITS[0]        = }")

    assert SHAPES('SQUARE') == SHAPES['SQUARE']
    assert FRUITS(3) == FRUITS[3]
    assert FRUITS['MANGO'] == FRUITS('MANGO')
    assert FRUITS[0] == FRUITS(0)
    try:
        FRUITS[99]
    except Exception as e:
        assert isinstance(e, ValueError)

    try:
        FRUITS(99)
    except Exception as e:
        assert isinstance(e, ValueError)
    try:
        FRUITS["99"]
    except Exception as e:
        assert isinstance(e, ValueError)
    try:
        FRUITS("99")
    except Exception as e:
        assert isinstance(e, ValueError)

    colors: list[int] = [COLOR.RED, COLOR.BLUE, COLOR.GREEN]
    for color in colors:
        match color:
            case COLOR.RED:
                print("Matched RED color")
            case COLOR.BLUE:
                print(f"Matched {COLOR[color]} color")
            case _:
                print(f"Sorry, couldn't match {COLOR(color)}")
