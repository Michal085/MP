import functools
import time


def print_with_separator(text: str) -> None:
    """Na oddelovani mezi ruznymi oddily"""
    print(120 * "*")
    print("")
    print(text)
    print("")
    print(120 * "*")


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


# Odkomentujte, pokud si chcete trochu pospat
# r = sleeper(1.2)
# print(r)


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

CHALLENGE_7 = """\
Pokuste se mi co nejdetailneji popsat, co se deje ve funkcich sum_/prod_/ ...

- Kolik maji tyto funkce parametru?
- Kolik ma parametru funkce `reduce`?
- Jake typy jsou parametry funkce `reduce`?

https://docs.python.org/3/library/functools.html?highlight=functools#functools.reduce
"""


sum_ = lambda lst: functools.reduce(lambda a, b: a + b, lst, 0)  # Emuluje builtins.sum
prod_ = lambda lst: functools.reduce(lambda a, b: a * b, lst, 1)  # Emuluje math.prod
min_ = lambda lst: functools.reduce(lambda a, b: min(a, b), lst)  # Emuluje buitins.min
max_ = lambda lst: functools.reduce(lambda a, b: max(a, b), lst)  # Emuluje buitins.max

# print(sum_([1, 2, 3, 4]))  # Vytiskne 10
# print(prod_([1, 2, 3, 4]))  # Vytiskne 24 - 4*3*2*1*1

print_with_separator(CHALLENGE_7)


CHALLENGE_8 = """\
    - Jak vypada kwargs, kdyz nevyplnime zadne pojmenovane argumenty?
    - Co se stane, kdyz zadame pojmenovany argument 2x, tj.

    ```
    zrava_funkce(x=1, x=2)
    ```

    - Co se stane, kdyz zadame pojmenovane argumenty pred pozicnimi?

"""


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


print_with_separator(CHALLENGE_8)
