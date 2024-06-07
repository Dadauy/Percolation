import random
import sys
import math

sys.setrecursionlimit(10000)


class CirclePercolation:
    lst_inf_per = [(), (7, 6, 5, 3, 4), (7, 6, 5), (7, 6, 5, 1, 8), (1, 8, 7), (1, 2, 3, 8, 7), (1, 2, 3),
                   (1, 2, 3, 4, 5), (3, 4, 5)]

    def __init__(self, size: int):
        self.a, self.cell, self.answer = self.generator_percolation(size)
        self.size = size

    class Circle:
        __slots__ = ("x", "y", "inf_per", "idx", "color", "neighbours")

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
                self.color = circle.color
                break
        used = [0] * len(a)
        self.dfs(len(a) - 1, used, a)
        # dct = dict()
        # for c in a:
        #     if c.color in dct:
        #         dct[c.color] += 1
        #     else:
        #         dct[c.color] = 0
        answer = (len(a) * (math.pi * (size ** 2))) / (850 ** 2)
        return a, cell, answer
