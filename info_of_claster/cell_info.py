def info_cell(parent, percolation, color_lst, x, y):
    start_x = 400
    start_y = 60
    radius = 800 / (2 * percolation.size - 1)
    if 400 <= x <= 1200 and 50 <= y <= 850:
        parent.flag_info = True
        i, j = int((x - start_x + radius / 2) // (2 * radius)), int((y - start_y + radius / 2) // (2 * radius))
        i += 1
        j += 1
        parent.color_claster = color_lst[percolation.a[j][i]]

    parent.repaint()
