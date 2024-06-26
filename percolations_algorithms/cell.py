import random
import copy
import numpy


class SquarePercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size, self.size_claster, self.center_mass, self.radius_claster = self.generator_percolation(
            size,
            probability)

    def f(self, cell, n):
        if cell[n] == n:
            return n
        while cell[n] != n:
            n = cell[n]
        return n

    def generator_percolation(self, size: int, probability: float):
        a = numpy.array([numpy.array([1 if ((not (random.uniform(0, 1) > probability)) and i != 0 and j != 0) else 0
                                      for i in range(0, size + 2)])
                         for j in range(0, size + 2)])
        cell = numpy.array([0])
        for i in range(1, size + 2):
            a[i][size + 1] = 0
            a[size + 1][i] = 0
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
                        a[i][j] = self.f(cell, a[i - 1][j])
                    else:
                        one = self.f(cell, a[i - 1][j])
                        two = self.f(cell, a[i][j - 1])
                        a[i][j] = min(one, two)
                        cell[max(one, two)] = a[i][j]

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                if a[i][j]:
                    proper = a[i][j]
                    while cell[proper] != proper:
                        proper = cell[proper]
                    a[i][j] = proper

        center_mass = [[0, 0] for i in range(len(cell))]
        radius_claster = [0 for i in range(len(cell))]
        radius_claster_size = [0 for i in range(len(cell))]
        size_claster = [0 for i in range(len(cell))]
        for i in range(1, size + 1):
            for j in range(1, size + 1):
                size_claster[a[i][j]] += 1
                center_mass[a[i][j]][0] += j - 1
                center_mass[a[i][j]][1] += size - i

        for i in range(len(cell)):
            if size_claster[i] != 0:
                center_mass[i][0] /= size_claster[i]
                center_mass[i][1] /= size_claster[i]

        for i in range(1, size + 1):
            for j in range(1, size + 1):
                if not ((a[i][j] == a[i - 1][j] and a[i][j] == a[i + 1][j]) or
                        (a[i][j] == a[i][j - 1] and a[i][j] == a[i][j + 1])):
                    radius_claster[a[i][j]] += (((center_mass[a[i][j]][0] - (j - 1)) ** 2) + (
                            (center_mass[a[i][j]][1] - (size - i)) ** 2)) ** 0.5
                    radius_claster_size[a[i][j]] += 1

        for i in range(len(cell)):
            if radius_claster_size[i] != 0:
                radius_claster[i] /= radius_claster_size[i]

        return a, cell, size, size_claster, center_mass, radius_claster
