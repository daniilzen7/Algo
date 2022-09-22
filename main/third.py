import numpy as np


def numpy_fizzbuzz(N: int) -> str:
    integers = np.arange(N)
    result = np.arange(N).astype(str)

    # Find indices in 'integers' that are divisible by 3 and 5
    mod_3 = np.argwhere(integers % 3 == 0)
    mod_5 = np.argwhere(integers % 5 == 0)

    # If a number is divisible by 3 and 5, it is also divisible by 15
    mod_15 = np.intersect1d(mod_3, mod_5, assume_unique=True)

    # Update results at corresponding indices
    result[mod_3] = 'fizz'
    result[mod_5] = 'buzz'
    result[mod_15] = 'fizzbuzz'

    return " ".join(result)