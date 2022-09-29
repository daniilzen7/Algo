import numpy as np


def numpy_fizzbuzz(N: int) -> str:
    integers = np.arange(N)
    result = np.arange(N).astype(str)

    # Находим индексы в 'integers' которые делятся на 3 и 5
    mod_3 = np.argwhere(integers % 3 == 0)
    mod_5 = np.argwhere(integers % 5 == 0)

    # Если число делится на 3 и 5, то оно делится и на 15
    mod_15 = np.intersect1d(mod_3, mod_5, assume_unique=True)

    # Обновляем результаты по соответствующим индексам
    result[mod_3] = 'fizz'
    result[mod_5] = 'buzz'
    result[mod_15] = 'fizzbuzz'

    return " ".join(result)
