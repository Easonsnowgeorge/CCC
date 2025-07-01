crystal = [(1, 0), (2, 0), (3, 0), (2, 1)]  # (x, y) locations for where  the crystals are
possible = [(1, 1), (3, 1), (2, 2)]  # locations where there might be a crystal if you zoom in more


def is_crystal(x, y, m):
    while m > 0:
        dimensions = 5 ** (m - 1)  # length of current magnification divided by 5, use this to get new x and y
        base_x = x // dimensions  # the x, y position if you zoom OUT by 1 magnification (x5)
        base_y = y // dimensions

        # current cell is a crystal
        if (base_x, base_y) in crystal:
            return True

        # might be a crystal, zoom in more
        elif (base_x, base_y) in possible:
            x %= dimensions  # get the new x and y positions
            y %= dimensions
            m -= 1

        else:  # no crystal area
            break

    return False  # can't zoom in further, so no crystal


for _ in range(int(input())):
    m, x, y = map(int, input().split())
    if is_crystal(x, y, m):
        print("crystal")
    else:
        print("empty")