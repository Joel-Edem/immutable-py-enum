# Immutable Python Enums 
A cursed implementation of enums in python.

## Usage
```python
import Enum

COLOR = Enum("RED", "BLUE", "GREEN", PINK=99)

colors = [COLOR.RED, COLOR.BLUE, COLOR.GREEN, COLOR.PINK]
for color in colors:
    match color:
        case COLOR.RED:
            print("Matched RED color")
        case COLOR.BLUE:
            print(f"Matched {COLOR[color]} color")
        case _:
            print(f"Sorry, couldn't match {COLOR(color)}")

```


### Output
```shell
Matched RED color
Matched BLUE color
Sorry, couldn't match GREEN
```


## Using Enums
With enums you can easily use the `.` or `[]` operator like classes or dicts, 
with the benefit of immutability and much faster lookups.

### Creating
```python
COLOR =  Enum("RED", "BLUE", "GREEN")
SHAPES = Enum(SQUARE=5, RECTANGLE=6, CIRCLE=9)
FRUITS = Enum("ORANGE", "BANANA", MANGO=2, LEMON=0)


```

### READING LABELS
```python
# by calling        PRINTS
print(FRUITS(2))   #   'MANGO'
print(SHAPES(9))   #   'CIRCLE'

# by index
print(FRUITS[0])    #  'LEMON'
print(SHAPES[9])    #   'CIRCLE'
```
### READING VALUES
```python
# BY INDEX
print(SHAPES['SQUARE'])  # 5
print(FRUITS['MANGO'])   # 2
# BY CALLING
print( FRUITS('MANGO'))  # 2    
print( FRUITS('LEMON'))  # 0
# BY ATTRIBUTE
print(FRUITS.BANANA)     # 4
print(COLOR.BLUE)        # 1

```


