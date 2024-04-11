import random
import numpy
import sys


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