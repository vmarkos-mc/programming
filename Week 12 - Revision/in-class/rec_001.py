# in-class/rec_001.py

from timeit import timeit

# The `typing` module is used to make type declarations
from typing import List, Callable  # For Python 3.8- compatibility


def loop_sum(ls: List[float]) -> float:
    """Computes the sum of a list of floats using a loop."""
    s = 0.0
    for x in ls:
        s = s + x
    return s


def rec_sum(ls: List[float]) -> float:
    """Computes the sum of a list of floats using recursion."""
    # Base case: if ls == []
    if not ls:  # Equivalent to `if len(ls) == 0:`
        return 0.0
    # Main case: if the list is not empty:
    #   * Pop the first element and add it to:
    #   * the sum of the rest.
    return ls[-1] + rec_sum(ls[:-1])
    # return ls[0] + rec_sum(ls[1:]) # Equivalent to the above


def time(*functions: List[Callable[[List[float]], float]]) -> List[float]:
    a = list(range(100))
    times = []
    for fn in functions:
        t = timeit(lambda: fn(a), number=1000)
        times.append(t)
    return times


def test() -> None:
    """Main entry point of our program."""
    a = [3, 2, 8, 9.5]
    # a: List[float] = list(range(1000)) # This should fail on a typical machine
    s = loop_sum(a)
    r = rec_sum(a)
    print(f"The loop sum of [{', '.join(map(str, a))}] is:      {s}.")
    print(f"The recursive sum of [{', '.join(map(str, a))}] is: {r}.")


def main() -> None:
    times = time(loop_sum, rec_sum)
    print(f"Loop time:       {times[0]}\n" f"Recursion time:  {times[1]}")


if __name__ == "__main__":
    main()
