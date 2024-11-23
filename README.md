# Immutable Python Enums 
A cursed implementation of enums in python.

## Usage
```python
import Enum

COLOR = Enum("RED", "BLUE", "GREEN")

colors = [COLOR.RED, COLOR.BLUE, COLOR.GREEN]
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

```python
COLOR = Enum("RED", "BLUE", "GREEN")

# using the .
blue = COLOR.BLUE  # get val

# using a string
blue_2 = COLOR['BLUE']

```

## Example USAGE 

```python

    print(f"{COLOR}\n")  # print enum
    #
    print(f"{COLOR.BLUE=}")  # get val
    #
    print(f"{COLOR(1)=}")  # get "enum label"
    #
    print(f'{COLOR["RED"]=}')  # get value
    #
    print(f"{COLOR[0]=}")  # get label
```

Output:
```shell
Enum:
 RED      0  
 BLUE     1  
 GREEN    2  

COLOR.BLUE=1
COLOR(1)='BLUE'
COLOR["RED"]=0
COLOR[0]='RED'
```