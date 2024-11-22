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
## Motivation

Pythons simplicity is its biggest asset in my opinion. 
How ever the lack of `enum` types is very much an oversight in my 
personal opinion. Over the years, Guido and the community have battled to find
a "pythonic" way to include `enum`'s into the python standard libray. 
After a long search, they landed on "Structural pattern matching".... which are clearly not enums.
While the new structural pattern matching provides powerful features not afforded by enums alone,
they also lack the simplicity of boring old enums with switch cases. 
And most importantly, lack the enum part.

> [!NOTE] TLDR; Yes I do know about structural pattern matching in python. 
> It still however, does not let you create enums. This addresses the enum part of the equation.

It is vary common to want to group options into some sort of structure.
This helps keeps code organized and prevents proliferation of random magic 
numbers throughout your code base. 
In python the most common go-to's are `Class/Dataclass` or `dicts` and even more obscurely, `range`
### examples
```python
# Using Classes
class COLORS:
  RED =   0
  BLUE =  1
  GREEN = 2


# Using Dicts
COLORS = {
  "RED" :  0,
  "BLUE":  1,
  "GREEN": 2
}

# Using rage
RED, BLUE, GREEN = range(3)
```
While these methods are simple enough and usually suffice, 
they each come with various tradeoffs that make them less convenient in general. 
This Enum class hopes to address this.

## Issues with current solutions.

### Mutability
This is by far one of the biggest issues with the above solutions.
The values of the enums can be canged at runtime, usually by accident.
For instance you meant to check if the value matched but accidentally fat-fingered, now you've changed the value.

```python
class CMD:
  RESET = 0    
  SAVE =  1

def handle_save_command() -> bool:
    cmd = get_cmd()  # lets say this command returns 0
    ...
    # accidentally mutating enum
    CMD.SAVE = cmd  # should be:  CMD.RESET == cmd .
```
The same mutability problems occur with dictionaries and ranges. Worse still, 
more enum options can be added at runtime accidentally or intentionally. 

Consider the example below:
```python
PAYMENT_TIERS = {
    "GOLD": 0,
    "SILVER": 1,
}

if PAYMENT_TIERS.get("GOLD"):  # subtle bug
    print("THIS STATEMENT IS UNREACHABLE")

```
It is very common to check if a key exists before accessing a member of a dict. 
It is also common and conveninent to use the `get` method to perform this check as it rerturns
`False` or your provided default, if the key does not exist.
While this method is convenient, it is not meant to be used to check for memebership **alone**,
but also return a default value. 
Hence if the key does indeed exist but the value it points to is Falsy, 
condition will evaluate to `False`. This poses an issue as no warning is provided either.

Heres a fix for the above btw (you should get in the habbit of)
```python
PAYMENT_TIERS = {
"GOLD": 0,
"SILVER": 1,
}

if "GOLD" in PAYMENT_TIERS:  # ALWAYS USE THE IN OPERATOR.
    print("THIS STATEMENT IS NOW REACHABLE")
```

### Label inconsistency
When using classes as enums, the 'labels' are just variables on the class. 
This means that it is not easy to check which value corresponds to a label 
without manually checking each variable on the class.

```python
class CMD:
  RESET = 0    
  SAVE =  1
  ...
  LAST_CMD = 78

def print_cmd(cmd:int):
    if cmd == CMD.RESET:
        print("RESET CMD")
    elif cmd == CMD.SAVE:
        print("SAVE CMD")
        ...
    elif cmd == cmd.LAST_CMD: # YOU literally have to enumerate each option since no `label` is attached to the enum value.
        ...

```
This problem is a little easier with dicts, but ranges are as tedious as classes
```python

PAYMENT_TIERS = {
"GOLD": 0,
"SILVER": 1,
}

def print_cmd(cmd: int):
    for tier, cmd_id in PAYMENT_TIERS.items():
        if cmd_id == cmd:
            print(f"{tier} Plan")
            return 

```

using Enums, its just 1 line
```python
COLOR = Enum("RED", "BLUE", "GREEN")

def print_cmd(col_id: int):
    label = COLOR(col_id) # get "enum label" by calling
    print(f"{label} Color")  

```
alternatively 
```python
COLOR = Enum("RED", "BLUE", "GREEN")

def print_cmd(col_id: int):   
    label = COLOR[col_id] # get label by index
    print(f"{label} Color")  
```
### Inconsistencies using the '.' 
Tied to the label issue is the '.' issue. Using dicts allows you to refer to the value using a string. 
so if you wanted to map a string name to an enum, you can do that easily. 
However, this double eged sword means that you can ONLY refer to the values using strings.
While the hash algos used should be fine, 
this does indeed add overhead and limits your flexibility to look up values.Above all, is easily error prone. 

The opposite is true for classes. 
While using the `.` is more convenient than dict lookups, you are trapped with the opposite problem.
If you received the name of the command, it is almost impossible to 'look up' the value.
You could use __getattr__ , or make another enum mapping the keys to strings,
adding yet more complexity and inconvenience.

### Error Prone and not fun
From the issues i've listed above it is pretty clear there are numerous pitfalls that render 
any of the above solutions incomplete at best. 


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






