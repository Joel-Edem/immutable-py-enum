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
    def __new__(cls, *args, **kwargs):
        if not args and not kwargs:
            raise Exception("Enum must have at least one key")

        if args and isinstance(args[0], tuple):
            args = args[0]

        keys = list(args)
        values = []
        if args:
            for v in args:
                if not isinstance(v, str):
                    raise Exception("Enum keys must be strings")
            if len(set(args)) != len(args):
                raise Exception("Duplicate Enum keys found")

            idx = max(kwargs.values()) + 1 if kwargs else 0
            for i in range(len(args)):
                values.append(idx)
                idx += 1

        if kwargs:
            for k, v in kwargs.items():
                keys.append(k)
                values.append(v)

        keys = tuple(keys)
        values = tuple(values)

        inst = super().__new__(cls, keys)
        inst._vals = values
        for idx, key in enumerate(inst):
            setattr(inst, str(key), inst._vals[idx])
        assert len(keys) == len(values)
        return inst

    def __call__(self, opt: int | str):
        try:
            if isinstance(opt, str):
                return self._vals[self.index(opt)]
            elif isinstance(opt, int):
                return super().__getitem__(self._vals.index(opt))
        except ValueError:
            raise ValueError("Enum.index(x): x not in enum")
        except Exception as e:
            raise e

    def __getitem__(self, opt: int | str):
        try:
            if isinstance(opt, str):
                return self._vals[self.index(opt)]
            else:
                return super().__getitem__(self._vals.index(opt))
        except ValueError:
            raise ValueError("Enum.index(x): x not in enum")
        except Exception as e:
            raise e

    def __repr__(self):
        m = len(max(self) * 2)
        return 'Enum:\n %s' % '\n '.join('{'f"{i}" f'[0]:<{m}}} ' ' {'f"{i}"'[1]}' for i in range(len(self))).format(
            *zip(self, self._vals))
