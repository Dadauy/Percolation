import random

import numpy


class TrianglePercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size_v, self.size_h = self.generator_percolation(size, probability)
        self.size = size

    @staticmethod
    def generator_percolation(size, probability):
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
