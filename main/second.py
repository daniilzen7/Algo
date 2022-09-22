from math import ceil
import itertools

def input_matrix(m, n):
    matrix = []
    for i in range(m):
        matrix.append([])
        new_l = list(map(int, input().split()))
        if len(new_l) == n:
            matrix[i].extend(new_l)
        else:
            raise Exception("число столбцов не соответствует введенным значениям")
    return matrix

def print_m(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print()


def transort(matrix):
    return [
        [matrix[j][i] for j in range(len(matrix))]
        for i in range(len(matrix[0]))
    ]


def multiply(P, K):
    if len(P[0]) != len(K):
        return Exception("Нельзя умножить эти матрицы")
    else:
        R = [[0 for i in range(len(K[0]))] for j in range(len(P))]
        for i in range(len(R)):
            for j in range(len(R[0])):
                # zip
                R[i][j] = sum([a * b for a, b in zip(P[i], [x[j] for x in K])])
        return R


def if_null(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                return False
            else:
                continue
    return True


def get_minor(matrix, m):
    ans = []
    for k in range(len(matrix[0])):
        ans.append([[matrix[i][j] for j in range(len(matrix[0])) if j != k] for i in range(len(matrix)) if i != m])
    return ans


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def get_opr(m):
    if len(m) != len(m[0]):
        raise ArithmeticError("m != n")
    else:
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        if len(m) == 3:
            return m[0][0] * m[1][1] * m[2][2] + m[2][0] * m[0][1] * m[1][2] + m[1][0] * m[2][1] * m[0][2] - m[2][0] * \
                   m[1][1] * m[0][2] - m[0][0] * m[2][1] * m[1][2] - m[1][0] * m[0][1] * m[2][2]
        else:
            ans = 0
            minors = get_minor(m, 0)
            # алгебраическое разложение
            for i in range(len(m[0])):
                ans += m[0][i] * get_opr(minors[i]) * (-1) ** (2 + i)
            return ans


def rank(matrix):
    if if_null(matrix):
        return 0
    # квадратная и не равна 0
    elif len(matrix) == len(matrix[0]) and get_opr(matrix) != 0:
        return len(matrix)
    else:
        # делаем больше строк чем столбцов если надо
        if len(matrix) < len(matrix[0]):
            matrix = transort(matrix)
        num = len(matrix[0])
        # рассмотрим все миноры
        all_minors = []
        if len(matrix) == len(matrix[0]):
            num -= 1
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    # если квадратная то получаем миноры вычеркиванием строк и столбцов
                    all_minors.append(getMatrixMinor(matrix, i, j))
        else:
            # если не квадратная то с помощью перебора вариантов получаем все возможные комбинации
            # строк (их всегда больше)
            all_minors = list(itertools.combinations(matrix, min(len(matrix), len(matrix[0]))))
        while num > 1:
            # начинаем перебор всех миноров и миноров миноров
            new_minor = []
            for minor in all_minors:
                # если максимальный минор не равен нулю то это ответ
                if get_opr(minor) != 0:
                    return num
                # не делаем для 2 потому что минор 2 это просто элементы
                if len(minor) != 2:
                    for i in range(len(minor)):
                        for j in range(len(minor)):
                            if getMatrixMinor(minor, i, j) not in new_minor:
                                new_minor.append(getMatrixMinor(minor, i, j))
            all_minors = new_minor
            num -= 1
        return num


def get_back(matrix):
    if len(matrix) != len(matrix[0]) != 3:
        raise Exception("не квадртаная матрица 3 порядка")
    else:
        new_matrix = [[0 for j in range(3)] for i in range(3)]
        print_m(new_matrix)
        det_A = get_opr(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = ((-1)**(2 + i + j)) * get_opr(getMatrixMinor(matrix, i, j))
        new_matrix = transort(new_matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_matrix[i][j] = new_matrix[i][j] / det_A
        return new_matrix

#matrix_x = [
#    [2, 3, 4, 5],
#    [0, -2, 3, 1],
#    [0, 2, 2, -4]
#]


#matrix_2 = [
#    [41, 433, -31, 123, 34, 0],
#    [-412, 244, 4221, 13, 4, 8],
#    [93, 0, 121, 93, 62, 55],
#    [-12, -15, 24, 7, -8, 533],
#    [912, 51, -81, 24, 0, 412],
#    [142, 812, 0, 512, -125, 15],
#    [615, -72, 71, 51, 6712, 15]
#]

var = input("a) транспортировать b) умножить c) определить ранг d) получить обратную матрицу\n")
if var in ["a", "b", "c", "d"]:
    m, n = map(int, input("Введите размер матрицы 1(m n)\n").split())
    print("Введите матрицу")
    matrix_1 = input_matrix(m, n)
    if var == "a":
        print_m(transort(matrix_1))
    if var == "b":
        p, k = map(int, input("Введите размер матрицы 2(m n)\n").split())
        print("Введите матрицу")
        matrix_2 = input_matrix(p, k)
        print_m(multiply(matrix_1, matrix_2))
    if var == "c":
        print(rank(matrix_1))
    if var == "d":
        print_m(get_back(matrix_1))
else:
    print("Ошибка")

