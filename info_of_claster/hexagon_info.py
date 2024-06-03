def info_hexagon(parent, percolation, color_lst, x, y):
    start_x = 400
    start_y = 60
    radius = 800 / percolation.size_v / 2
    distance = 700 / (2 + (3 / 2) * (percolation.size - 1) + ((1 / 2) if 2 <= percolation.size <= 6 else 0))
    distance_h = distance * ((3 ** (1 / 2)) / 2)
    if 400 <= x <= 1250 and 50 <= y <= 850:
        i = int((x - start_x + radius / 2) // distance_h)
        if i % 2 == 0:
            j = int((y - start_y - distance / 2) // distance) + 2
            j *= 4
            j //= 3
            j -= 1 if (j % 4) == 0 else 0
        else:
            j = int((y - start_y) // distance) + 1
            j *= 4
            j //= 3
        i += 1
        if percolation.a[j][i] != 0:
            parent.flag_info = True
            parent.color_claster = color_lst[percolation.a[j][i]]
            parent.cnt_v = percolation.size_claster[percolation.a[j][i]]
            parent.center_mass = percolation.center_mass[percolation.a[j][i]]
            parent.radius_claster = percolation.radius_claster[percolation.a[j][i]]
        else:
            parent.flag_info = False

    parent.repaint()
