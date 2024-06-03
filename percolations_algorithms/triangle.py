import random

import numpy


class TrianglePercolation:

    def __init__(self, size: int, probability: float):
        self.a, self.cell, self.size_v, self.size_h, self.size_claster, self.center_mass, self.radius_claster = self.generator_percolation(
            size, probability)
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

        center_mass = [[0, 0] for i in range(len(cell))]
        radius_claster = [0 for i in range(len(cell))]
        radius_claster_size = [0 for i in range(len(cell))]
        size_claster = [0 for i in range(len(cell))]
        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                a[i][j] = cell[a[i][j]]
                size_claster[a[i][j]] += 1
                center_mass[a[i][j]][0] += j - 1
                center_mass[a[i][j]][1] += size_v - i

        for i in range(len(cell)):
            if size_claster[i] != 0:
                center_mass[i][0] /= size_claster[i]
                center_mass[i][1] /= size_claster[i]

        for i in range(1, size_v + 1):
            for j in range(1, size_h + 1):
                radius_claster[a[i][j]] += (((center_mass[a[i][j]][0] - (j - 1)) ** 2) + (
                        (center_mass[a[i][j]][1] - (size_v - i)) ** 2)) ** 0.5
                radius_claster_size[a[i][j]] += 1

        for i in range(len(cell)):
            if radius_claster_size[i] != 0:
                radius_claster[i] /= radius_claster_size[i]

        return a, cell, size_v, size_h, size_claster, center_mass, radius_claster
