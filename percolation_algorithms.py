import random
import numpy
import collections


class SquarePercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size = self.generator_percolation(size, probability)

    def generator_percolation(self, size: int, probability: float):
        a = numpy.array([numpy.array([1 if ((not (random.uniform(0, 1) > probability)) and i != 0 and j != 0) else 0
                                      for i in range(0, size + 1)])
                         for j in range(0, size + 1)])
        cell = numpy.array([0])

        cnt = 1
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                if a[i][j]:
                    if a[i][j - 1] == a[i - 1][j] == 0:
                        cell = numpy.append(cell, [cnt])
                        a[i][j] = cell[cnt]
                        cnt += 1
                    elif a[i - 1][j] == 0:
                        a[i][j] = a[i][j - 1]
                    elif a[i][j - 1] == 0:
                        a[i][j] = a[i - 1][j]
                    else:
                        cell[max(a[i - 1][j], a[i][j - 1])] = min(a[i - 1][j], a[i][j - 1])
                        a[i][j] = a[i - 1][j] = a[i][j - 1] = min(a[i - 1][j], a[i][j - 1])

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                a[i][j] = cell[a[i][j]]

        return a, cell, size


class HexagonsPercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size_v, self.size_h = self.generator_percolation(size, probability)
        self.size = size

    def generator_percolation(self, size, probability):
        size_v = 4 + 2 * (size - 1)
        size_h = 3 + 2 * (size - 1) + (1 if size > 1 else 0)
        a = numpy.zeros((size_v + 2, size_h + 2), dtype=int)
        cell = numpy.array([0])
        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                if (((i - 1) % 4 == 0 or (i - 1) % 4 == 3) and (j - 1) % 2 == 1) or (
                        ((i - 1) % 4 == 1 or (i - 1) % 4 == 2) and (j - 1) % 2 == 0):
                    a[i][j] = 1 if not (random.uniform(0, 1) > probability) else 0

        cnt = 1
        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                if a[i][j]:
                    if ((j - 1) % 2 == 1 and (i - 1) % 4 == 0) or ((j - 1) % 2 == 0 and (i - 1) % 4 == 2):
                        if a[i - 1][j] == 0:
                            cell = numpy.append(cell, [cnt])
                            a[i][j] = cell[cnt]
                            cnt += 1
                        else:
                            a[i][j] = a[i - 1][j]
                    elif ((j - 1) % 2 == 1 and (i - 1) % 4 == 3) or ((j - 1) % 2 == 0 and (i - 1) % 4 == 1):
                        if a[i - 1][j - 1] == a[i - 1][j + 1] == 0:
                            cell = numpy.append(cell, [cnt])
                            a[i][j] = cell[cnt]
                            cnt += 1
                        elif a[i - 1][j - 1] == 0:
                            a[i][j] = a[i - 1][j + 1]
                        elif a[i - 1][j + 1] == 0:
                            a[i][j] = a[i - 1][j - 1]
                        else:
                            cell[max(a[i - 1][j - 1], a[i - 1][j + 1])] = min(a[i - 1][j - 1], a[i - 1][j + 1])
                            a[i][j] = a[i - 1][j - 1] = a[i - 1][j + 1] = min(a[i - 1][j - 1], a[i - 1][j + 1])

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                a[i][j] = cell[a[i][j]]

        return a, cell, size_v, size_h


class TrianglePercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size_v, self.size_h = self.generator_percolation(size, probability)
        self.size = size

    def generator_percolation(self, size, probability):
        size_v = (2 + size - 1) if size > 0 else 0
        size_h = (3 + size - 1) if size > 0 else 0
        a = numpy.zeros((size_v + 2, size_h + 2), dtype=int)
        cell = numpy.array([0])
        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                if ((i - 1) % 2 == 0 and (j - 1) % 2 == 1) or ((i - 1) % 2 == 1 and (j - 1) % 2 == 0):
                    a[i][j] = 1 if not (random.uniform(0, 1) > probability) else 0

        cnt = 1
        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                if a[i][j]:
                    if a[i - 1][j - 1] == a[i - 1][j + 1] == 0:
                        cell = numpy.append(cell, [cnt])
                        a[i][j] = cell[cnt]
                        cnt += 1
                    elif a[i - 1][j - 1] == 0:
                        a[i][j] = a[i - 1][j + 1]
                    elif a[i - 1][j + 1] == 0:
                        a[i][j] = a[i - 1][j - 1]
                    else:
                        cell[max(a[i - 1][j - 1], a[i - 1][j + 1])] = min(a[i - 1][j - 1], a[i - 1][j + 1])
                        a[i][j] = a[i - 1][j - 1] = a[i - 1][j + 1] = min(a[i - 1][j - 1], a[i - 1][j + 1])

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                a[i][j] = cell[a[i][j]]

        return a, cell, size_v, size_h


class CirclePercolation:

    def __init__(self, cnt: int, size: int):
        self.a, self.cell = self.generator_percolation(cnt, size)
        self.size = size

    class Circle:
        __slots__ = ("x", "y", "color")

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def intersection_circles(self):
            pass

    def generator_percolation(self, cnt, size):
        a = []
        cell = numpy.array([0])

        for i in range(cnt):
            pass
        return [], []
