# Copyright (c) 2024 Joel Ametepeh <JoelAmetepeh@gmail.com>
#
# This software is provided "as-is", without any express or implied warranty. In no event
# will the authors be held liable for any damages arising from the use of this software.
#
# Permission is granted to anyone to use this software for any purpose, including commercial
# applications, and to alter it and redistribute it freely, subject to the following restrictions:
#
#   1. The origin of this software must not be misrepresented; you must not claim that you
#   wrote the original software. If you use this software in a product, an acknowledgment
#   in the product documentation would be appreciated but is not required.
#
#   2. Altered source versions must be plainly marked as such, and must not be misrepresented
#   as being the original software.
#
#   3. This notice may not be removed or altered from any source distribution.

class Enum(tuple):
    def __new__(cls, *args):
        if not args:
            raise Exception("Enum must have at least one key")
        if isinstance(args[0], tuple):
            args = args[0]
        for v in args:
            if not isinstance(v, str):
                raise Exception("Enum keys must be strings")
        if len(set(args)) != len(args):
            raise Exception("Duplicate Enum keys found")
        return super().__new__(cls, args)

    def __init__(self, *args):
        super().__init__()
        self._sz = len(args)
        for idx, key in enumerate(self):
            setattr(self, str(key), idx)

    def __call__(self, val: int):
        assert isinstance(val, int)
        assert val
        return self[val]

    def __repr__(self):
        t = '\n '.join('{'f"{i}"'[0]:<5} ' ' {'f"{i}"'[1]:^5}' for i in range(len(self)))
        s = t.format(*zip(self, range(len(self))))
        return f'Enum:\n {s}'

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.index(index)
        return super().__getitem__(index)


if __name__ == "__main__":
    COLOR = Enum("RED", "BLUE", "GREEN")

    colors: list[int] = [COLOR.RED, COLOR.BLUE, COLOR.GREEN]
    for color in colors:
        match color:
            case COLOR.RED:
                print("Matched RED color")
            case COLOR.BLUE:
                print(f"Matched {COLOR[color]} color")
            case _:
                print(f"Sorry, couldn't match {COLOR(color)}")

    print(f"{COLOR}\n")  # print enum
    #
    print(f"{COLOR.BLUE=}")  # get val
    #
    print(f"{COLOR(1)=}")  # get "enum label"
    #
    print(f'{COLOR["RED"]=}')  # get value
    #
    print(f"{COLOR[0]=}")  # get label
