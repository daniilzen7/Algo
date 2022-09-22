from main import second
import numpy, timeit


matrix_1 = [
    [2, 5, 7],
    [6, 3, 4],
    [5, -2, -3]
]

matrix_2 = numpy.matrix("2, 5, 7; 6, 3, 4; 5, -2, -3")

start_time = timeit.default_timer()
second.get_back(matrix_1)
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
numpy.linalg.inv(matrix_2)
print(timeit.default_timer() - start_time)