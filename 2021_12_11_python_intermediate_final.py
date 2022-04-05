from __future__ import annotations

import enum
import functools
import time


def print_with_separator(text: str) -> None:
    """Na oddelovani mezi ruznymi oddily"""
    print(120 * "*")
    print("")
    print(text)
    print("")
    print(120 * "*")


BIG_CHALLENGE = """\
## Advent of Code den 2 část 1

Zjistit finální pozici ponorky po tom, co si pohybovala podle předepsaných instrukcí.

Instrukce jsou v souboru **day2.txt**. Každý řádek obsahuje právě jednu instrukci, která
vypadá jako `forward 5`, `down 3`, atd.

- `forward X` zvyšuje horizontální pozici o `X`
- `up X` **snižuje** hloubku o `X`
- `down X` **zvyšuje** hloubku o `X`

Začináme v horizontalání pozici 0 a hloubce taktéž 0.

Úkolem je zjistit součin hloubky a horizontalní pozice ponorky po vykonání všech pohybů.
"""

print_with_separator(BIG_CHALLENGE)


SOLUTION_OUTLINE = """\
Úlohu si rozdělíme na následující pod-problémy:

1. načtení řádku ze souboru
2. transformace (parsování) řádku do datové struktury reprezentující instrukci, se kterou
    se nám bude lépe pracovat
3. napsání procedury, která z instrukce a pozice vygeneruje novou pozici na základě pravidel
    v zadání.
4. Postupné aplikaci všech instrukcí na měnící se pozice, počínaje v (0, 0)

"""

print_with_separator(SOLUTION_OUTLINE)


CHALLENGE_1 = """\
### Úkol 1

Napište funkci `load_lines`, která na vstupu bere jméno souboru a na výstupu vrátí seznam
řádků souboru.

Dbejte na to, abyste nezapomněli soubor zavřít po tom, co jej otevřete. Co se stane, když
soubor neexistuje?

```
def load_lines(file_name: str) -> list[str]:
    ...
```

"""

print_with_separator(CHALLENGE_1)


def load_lines(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        commands = file.readlines()
    lst = []
    for i in commands:
        lst.append(i.rstrip("\n"))
    return lst


def load_lines_v2(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        lines = file.readlines()
        lst = [line.rstrip("\n") for line in lines]
        return lst


def load_lines_v3(file_name: str) -> list[str]:
    with open(file_name, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file.readlines()]


print(load_lines_v3("day2.txt"))


CHALLENGE_2 = """\
### Úkol 2

Napište funkci `parse_line`, která na vstupu bere řetězec a vrátí takovou strukturu,
která bude uchovávat v sobě informaci o instrukci, tj. jestli je `forward`, `down` nebo `up`
a o kolik jednotek se máme posunout - to musí být v každém případě `int`.

Výběr struktury nechám na vás, máte ale bžilion možností:

- objekt vámi vytvořené třídy Instruction
- dvojice
- seznam
- slovník
- ...

```
def parse_line(line: str):
    ...
```

PS: Možná by se vám hodila třída na výčty - enumerace - možností. Zde se můžete inspirovat
https://docs.python.org/3/library/enum.html?highlight=enum#creating-an-enum


"""

print_with_separator(CHALLENGE_2)

lines = load_lines("day2.txt")

instruction_line = lines[0]
print(instruction_line)


def parse_line_as_tuple(line: str) -> tuple[str, int]:
    split_by_spaces = line.split()
    return (split_by_spaces[0], int(split_by_spaces[1]))


def parse_line_as_list(line: str) -> list:
    split_by_spaces = line.split()
    return [split_by_spaces[0], int(split_by_spaces[1])]


def parse_line_as_dict(line: str) -> dict:
    split_by_spaces = line.split()
    instruction = {"direction": split_by_spaces[0], "units": int(split_by_spaces[1])}
    return instruction


 print(parse_line_as_tuple(instruction_line))
 print(parse_line_as_list(instruction_line))
 print(parse_line_as_dict(instruction_line))


def load_and_parse(file_name: str) -> list[tuple[str, int]]:
    return [parse_line_as_tuple(line) for line in load_lines(file_name)]


 print(load_and_parse("day2.txt"))


class Direction(enum.Enum):
    FORWARD = "forward"
    UP = "up"
    DOWN = "down"


direction1 = Direction("forward")

print(direction1)

if direction1 is Direction.DOWN:
    print("Jdeme dolu!")
else:
    print("Jdeme dopredu nebo nahoru!")

# Enum tridy chrani pred spatnym vstupem - at uz umyslne nebo neumyslne zadanym!
try:
    direction2 = Direction("forwerd")
except ValueError:
    print("Spatny smer!")


def parse_line_as_tuple_with_enum(line: str) -> tuple[Direction, int]:
    split_by_spaces = line.split()
    return (Direction(split_by_spaces[0]), int(split_by_spaces[1]))


print(parse_line_as_tuple_with_enum(instruction_line))


class Instruction:
    def __init__(self, direction, units):
        self.direction = direction
        self.units = int(units)


def parse_line_as_instruction(line: str) -> Instruction:
    split_by_spaces = line.split()
    instruction = Instruction(split_by_spaces[0], split_by_spaces[1])
    return instruction


instruction = parse_line_as_instruction(instruction_line)
print(instruction)
print(instruction.direction)
print(instruction.units)

CHALLENGE_3 = """\
### Úkol 3

Napište funkci `move`, která má 2 parametry - `instruction` vyjadřující instrukci a
`position` vyjadřující pozici a vrací novou pozici, kterou získáme aplikováním
instrukce podle zadání na `position`.

Výběr reprezentace pozice nechám na vás, máte ale bžilion možností:

- objekt vámi vytvořené třídy Position
- dvojice
- seznam
- slovník
- dataclass
- ...

```
def move(instruction, position):
    ...
```

"""


def move(instruction: tuple[str, int], position: tuple[int, int]) -> tuple[int, int]:
    if instruction[0] == "forward":
        new_position = (position[0] + instruction[1], position[1])
    elif instruction[0] == "up":
        new_position = (position[0], position[1] - instruction[1])
    elif instruction[0] == "down":
        new_position = (position[0], position[1] + instruction[1])

    return new_position


instruction_as_tuple = parse_line_as_tuple(instruction_line)

print(instruction_as_tuple)

# Chci, aby tohle vracelo (5, 0)
print(move(instruction_as_tuple, (0, 0)))

print(move(("up", 10), (100, 50)))  # Vytiskne (100, 40)

CHALLENGE_4 = """\
### Úkol 4

Napište funkci `follow_instructions`, která ma 2 parametry - seznam instrukcí a výchozí pozici.

Výstupem je pak pozice, na kterou se dostaneme, pokud postupně aplikujeme všechny instrukce ze
seznamu, počínaje výchozí pozicí.

```
def follow_instructions(instructions, initial_position):
    ...
```

"""

print_with_separator(CHALLENGE_4)


def follow_instructions(
    instructions: list[tuple[str, int]],
    position: tuple[int, int],
) -> tuple[int, int]:
    new_position = position

    for instruction in instructions:
        new_position = move(instruction, new_position)

    return new_position


instructions = load_and_parse("day2.txt")

print(instructions)

final_position = follow_instructions(instructions, (0, 0))

print(final_position)

print(f"Solution part 1: {final_position[0] * final_position[1]}")


def follow_instructions_v2(
    instructions: list[tuple[str, int]],
    position: tuple[int, int],
) -> tuple[int, int]:
    """
    https://docs.python.org/3/library/functools.html?highlight=functools#functools.reduce

    Obecny koncept, kdyz chceme pole redukovat na 1 prvek.
    """
    return functools.reduce(lambda pos, instr: move(instr, pos), instructions, position)


print(follow_instructions_v2(instructions, (0, 0)))

# Na hrani ;)
sum_ = lambda lst: functools.reduce(lambda a, b: a + b, lst, 0)  # Emuluje builtins.sum
prod_ = lambda lst: functools.reduce(lambda a, b: a * b, lst, 1)  # Emuluje math.prod
min_ = lambda lst: functools.reduce(lambda a, b: min(a, b), lst)  # Emuluje buitins.min
max_ = lambda lst: functools.reduce(lambda a, b: max(a, b), lst)  # Emuluje buitins.max

 print(sum_([1, 2, 3, 4]))  # Vytiskne 10
 print(prod_([1, 2, 3, 4]))  # Vytiskne 24 - 4*3*2*1*1

print_with_separator("")

WHAT_IS_DECORATOR = """\
## Co je to dekorátor?

Funkce, která má 1 parametr - jinou funkci - jejíž funkcionalitu nějakým
způsobem rozšiřuje.

Použití:

- chceme vypsat, jak dlouho trval běh funkce
- chceme vypsat argumenty volané funkce za běhu programu
- chceme omezit, jak často se může nějaká funkce volat (třeba max. 5 za sekundu)
- cachování
- ...

Mustr, jak psát dekorátory:

```
def my_decorator(func):

    # `inner` je definice funkce ve funkci, tzv. `closure`
    def inner(*args, **kwargs):
        # ^ jelikoz nevime, co mohou mit dekorovane funkce za parametry, davame zde *args, **kwargs

        ...

        result = func(*args, **kwargs)

        ...

        return result

    # Vracime funkci!
    return inner
```

Glosář: https://docs.python.org/3/glossary.html#term-decorator
"""

print_with_separator(WHAT_IS_DECORATOR)


def time_it(func):
    # @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.monotonic()
        result = func(*args, **kwargs)
        t1 = time.monotonic() - t0
        print(f"Execution of function {func.__name__} took {t1:.4} seconds!")
        return result

    return inner


@time_it
def sleeper(x):
    """
    Just take a nap for x seconds.
    """

    time.sleep(x)
    return x


# Odkomentujte, pokud si chtete trochu pospat
 r = sleeper(1.2)
 print(r)


def zrava_funkce(*args, **kwargs):
    """
    Tehle funkci je uplne jedno, kolik ji date argumentu, jestli jsou pozicni nebo
    pojmenovane.

    Vsechny pozicni zachyti do **n-tice** args.
    Vsechny pojmenovane zachyti do **slovniku** kwargs.

    Pojmenovani args/kwargs je konvence, videl jsem i *arguments nebo **kws.
    """

    print(f"Pozicni argumenty: {args}")
    print(f"Pojmenovane argumenty: {kwargs}")


 f(1, 2)
 f(1, 2, 3, 4, x=1, y=2, z=3)
 ...


CHALLENGE_5 = """\
Napište dekorátor `praskac`, který u každé funkce vypíše, co při zavolání měla
za argumenty a co vrátila.

```
def praskac(func):
    def inner(*args, **kwargs):
        ...

    return inner
```
"""

print_with_separator(CHALLENGE_5)

CHALLENGE_6 = '''\

Napište funkci `intersect`, která na vstupu bere 2 seznamy čísel a vrátí seznam takových
čísel, které se vyskytují v obou z nich.

```
def intersect(lst1: list[float], lst2: list[float]) -> list[float]:
    """
    >>> intersect([1, 2, 3], [3, 4, 5])
    [3]
    >>> intersect([1, 2], [3, 4])
    []
    """
    ...
```

**BONUS**: Použijte na ni dekorátor `time_it`. Jak se bude čas měnit, budou-li mít pole řádově
stovky prvků? Tisíce? Desetitisíce?
'''
print_with_separator(CHALLENGE_6)
