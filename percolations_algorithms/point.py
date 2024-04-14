import collections
import math
import random
import sys

sys.setrecursionlimit(10000)


class RandomPointPercolation:
    lst_inf_per = [(), (7, 6, 5, 3, 4), (7, 6, 5), (7, 6, 5, 1, 8), (1, 8, 7), (1, 2, 3, 8, 7), (1, 2, 3),
                   (1, 2, 3, 4, 5), (3, 4, 5)]

    def __init__(self, probability):
        self.a, self.cell = self.generator_percolation(probability)

    class Point:
        __slots__ = ("x", "y", "color", "inf_per", "idx", "neighbours")

        def __init__(self, x, y, idx):
            self.x = x
            self.y = y
            self.color = -1
            self.inf_per = 0
            self.idx = idx
            self.neighbours = []

        def __repr__(self):
            return f"P({self.x}, {self.y})"

    @staticmethod
    def on_border(point: Point):
        size = 1
        x = point.x
        y = point.y
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

    def dfs_for_inf_percolation(self, point: Point, inf_per, used, a):
        used[point.idx] = 1
        for circle_u in point.neighbours:
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

    @staticmethod
    def if_connect(probability):
        if not random.random() > probability:
            return True
        return False

    @staticmethod
    def new_cord(x, y, a, b, c, sector) -> (int, int):
        line = c * (1200 / 1)
        angle = (360 / a) * (sector + 1) * b + (360 / a) * sector
        n_x = x + math.cos(math.radians(angle)) * line
        n_y = y + math.sin(math.radians(angle)) * line
        return n_x, n_y

    def generator_percolation(self, probability):
        point = self.Point(425, 425, 0)
        point.color = 0
        a = [point]
        cell = [1]
        cell_cnt = 1
        cnt = 0
        q = collections.deque()
        q.append(point)
        while q:
            point = q.popleft()
            used = [0] * len(a)
            if point.inf_per and self.dfs_for_inf_percolation(point, point.inf_per, used, a):
                break
            a_r = random.randint(1, 5)
            connect = False
            for sector in range(a_r):
                b = random.random()
                c = random.random()
                new_x, new_y = self.new_cord(point.x, point.y, a_r, b, c, sector)
                cnt += 1
                new_point = self.Point(new_x, new_y, cnt)
                new_point.inf_per = self.on_border(new_point)
                if self.if_connect(probability):
                    connect = True
                    point.neighbours.append(new_point.idx)
                    new_point.idx = point.idx
                    new_point.color = point.color
                else:
                    cell_cnt += 1
                    cell.append(cell_cnt)
                    new_point.color = cell_cnt
                a.append(new_point)
                if new_x < 0 or new_x > 850 or new_y < 0 or new_y > 850:
                    pass
                else:
                    q.append(new_point)
            if not connect:
                break

        used = [0] * len(a)
        for i in range(len(a)):
            if not used[i]:
                self.dfs(i, used, a)

        return a, cell
