from typing import Callable, TypeVar, Union

one_string: str = 'string'
one_integer: int = 1
one_float: float = 1.23
one_boolean: bool = True
one_set: set = {1, 2, 3}
one_list: list = []
one_dict: dict = {}
one_tuple: tuple = (1, 2, 3)


print(type(one_string))
print(type(one_integer))
print(type(one_float))
print(type(one_boolean))
print(type(one_set))
print(type(one_list))
print(type(one_tuple))

# mypy main.py -> 'main.py:20: error: Incompatible types in assignment (expression has type "int", variable has type "str")'
one_string = 1

list_string: list[str] = ['a', 'b', 'c']
list_tuple: list[tuple] = [(1, 'a'), (2, 'b')]
list_list_int: list[list[int]] = [[1], [1, 2]]

# mypy main.py ->
# main.py:29: error: List item 0 has incompatible type "int"; expected "List[int]"
# main.py:29: error: List item 1 has incompatible type "int"; expected "List[int]"
list_list_int = [1, 2]

# Type alias
ListInt = list[int]  # Type alias ListInt
DictListInt = dict[str, ListInt]  # Type alias DictListInt

one_dict_list_int: DictListInt = {'A': [1, 2], 'B': [3, 4], 'C': [5, 6]}

# mypy main.py -> main.py:45: error: List item 1 has incompatible type "str"; expected "int"
one_dict_list_int = {'A': [1, 2], 'B': [3, 4], 'C': [5, 'A']}

# Python >= 3.10
# string_and_int: str | int = 1  # Union
# Python < 3.10
string_and_int: Union[str, int] = 1  # Union
string_and_int = 1  # No error
string_and_int = 'A'  # No error

# mypy main.py -> main.py:60: error: Incompatible types in assignment (expression has type "float", variable has type "Union[str, int]")
string_and_int = 1.5


def mySum(x: int, y: Union[int, float, None] = None):
    if isinstance(y, float) or isinstance(y, int):
        return x + y
    else:
        return x


mySum(1, 1)

mySum(1, 1.2)

mySum(1, None)
# mypy main.py -> main.py:76: error: Argument 2 to "mySum" has incompatible type "str"; expected "Union[int, float, None]"
mySum(1, 'A')

# Callable ##
SumInt = Callable[[int, int], int]


def execute(func: SumInt, a: int, b: int) -> int:
    return func(a, b)


def other_sum(a: int, b: int) -> int:
    return a + b


execute(other_sum, 1, 2)


def other_sum2(a: float, b: float) -> float:
    return a + b


# mypy main.py -> main.py:98: error: Argument 1 to "execute" has incompatible type "Callable[[float, float], float]"; expected "Callable[[int, int], int]"
execute(other_sum2, 1, 1)


# TypeVar
T = TypeVar('T')


def get_item(list_items: list[T], index: int) -> T:
    return list_items[index]


get_item([1, 2, 3, 4], 2)
