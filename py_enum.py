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
from collections import namedtuple


def simple_enum(*args, **kwargs):
    _keys = [*args, *kwargs.keys()]
    assert len(set(_keys)) == len(_keys), "Duplicate Enum keys found"
    for k in _keys:
        assert isinstance(k, str), "Enum keys must be strings"
    _t = namedtuple("Enum", _keys)
    _v = []

    idx = max(kwargs.values()) + 1 if kwargs else 0
    for i in range(len(args)):
        _v.append(idx)
        idx += 1
    for kw in kwargs:
        _v.append(kwargs[kw])
    return _t(*_v)


class Enum:
    def __new__(cls, *args, **kwargs):
        inst = simple_enum(*args, **kwargs)
        return inst

