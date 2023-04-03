import typing

def all_combinations(*iterables: typing.Iterable) -> typing.Generator[tuple[typing.Any], None, None]:
    iterables = tuple(filter(lambda i: (len(i) > 0), iterables))
    if len(iterables) == 0:
        return
    elif len(iterables) == 1:
        for x in iterables[0]:
            yield (x,)
    else:
        for x in iterables[0]:
            for y in all_combinations(*iterables[1:]):
                yield (x,) + (y if isinstance(y, tuple) else (y,))

if __name__ == "__main__":
    for c in all_combinations([1, 2], [], [3, 4], [], [7, 8, 9]):
        print(c)
