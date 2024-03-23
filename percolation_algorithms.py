import random
import numpy
import collections
import sys

sys.setrecursionlimit(10000)


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

    def __init__(self, size: int):
        self.lst_inf_per = [(), (7, 6, 5, 3, 4), (7, 6, 5), (7, 6, 5, 1, 8), (1, 8, 7), (1, 2, 3, 8, 7), (1, 2, 3),
                            (1, 2, 3, 4, 5), (3, 4, 5)]
        self.a, self.cell = self.generator_percolation(size)
        self.size = size

    class Circle:
        __slots__ = ("x", "y", "color", "inf_per", "idx", "neighbours")

        def __init__(self, x, y, idx):
            self.x = x
            self.y = y
            self.color = -1
            self.inf_per = 0
            self.idx = idx
            self.neighbours = []

        def __repr__(self):
            return f"C({self.x}, {self.y}, {self.color})"

    def intersection_circles(self, first_circle: Circle, second_circle: Circle, r):
        EPS = 0.00001
        x2, y2 = second_circle.x - first_circle.x, second_circle.y - first_circle.y
        a = -2 * x2
        b = -2 * y2
        c = x2 ** 2 + y2 ** 2
        if (c * c) > (r * r * (a * a + b * b) + EPS):
            return False
        return True

    def on_border(self, circle, size):
        x = circle.x
        y = circle.y
        if x <= size:
            if y <= size:
                return 1
            elif y >= (850 - size):
                return 7
            else:
                return 8
        elif x >= (850 - size):
            if y <= size:
                return 3
            elif y >= (850 - size):
                return 5
            else:
                return 4
        elif y <= size:
            return 2
        elif y >= (850 - size):
            return 6
        return 0

    def dfs_for_inf_percolation(self, circle: Circle, inf_per, used, a):
        used[circle.idx] = 1
        for circle_u in circle.neighbours:
            if a[circle_u].inf_per in self.lst_inf_per[inf_per]:
                return True
            if not used[a[circle_u].idx]:
                return self.dfs_for_inf_percolation(a[circle_u], inf_per, used, a)

    def dfs(self, v, used, a):
        used[v] = 1
        for u in a[v].neighbours:
            if not used[u]:
                a[u].color = a[v].color
                self.dfs(u, used, a)

    def generator_percolation(self, size):
        a = []
        cell = []
        cnt = 1
        while True:
            x, y = random.randint(0, 850), random.randint(0, 850)
            circle = self.Circle(x, y, len(a))
            circle.inf_per = self.on_border(circle, size)
            for i in range(len(a)):
                if self.intersection_circles(circle, a[i], size):
                    circle.color = a[i].color
                    circle.neighbours.append(a[i].idx)
                    a[i].neighbours.append(circle.idx)
            if circle.color == -1:
                circle.color = cnt
                cell.append(cnt)
                cnt += 1
            a.append(circle)
            used = [0] * len(a)
            if circle.inf_per and self.dfs_for_inf_percolation(circle, circle.inf_per, used, a):
                break
        used = [0] * len(a)
        for i in range(len(a)):
            if not used[i]:
                self.dfs(i, used, a)
        # print((len(a) * (3.14 * (size ** 2))) / (850 ** 2))
        return a, cell
