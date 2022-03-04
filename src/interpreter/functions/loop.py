from typing import List

from src.interpreter.expression import Expression


def loop(block: List, codebase):
    repeats = Expression(block[1], codebase)
    functions = block[2:]
    results = []
    for _ in range(repeats):
        for func in functions:
            result = Expression(func, codebase)
            if result is not None:  # VOID Function
                results.append(result)

    if results:
        return results
