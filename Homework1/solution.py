def traverse(to_traverse, y_path, x_path):
    to_return = []
    for y in y_path:
        column = []
        for x in x_path:
            column.append(to_traverse[x][y])
        to_return.append(column)
    return to_return


def rotate_left(to_rotate):
    return traverse(
        to_rotate,
        range(len(to_rotate) - 1, -1, -1),
        range(len(to_rotate[0])))


def rotate_right(to_rotate):
    return traverse(
        to_rotate,
        range(len(to_rotate[0])),
        range(len(to_rotate) - 1, -1, -1))


def map_pic(func, pic):
    return [[func(rgb) for rgb in col] for col in pic]


def inv(rgb):
    return tuple(255 - x for x in rgb)


def invert(to_invert):
    return map_pic(inv, to_invert)


def light(rgb, ratio):
    return tuple(x + int(ratio*(255 - x)) for x in rgb)


def dark(rgb, ratio):
    return tuple(int(x*(1 - ratio)) for x in rgb)


def lighten(to_lighten, ratio):
    return map_pic(lambda x: light(x, ratio), to_lighten)


def darken(to_darken, ratio):
    return map_pic(lambda x: dark(x, ratio), to_darken)


def create_histogram(to_create_from):
    to_return = dict(red={}, green={}, blue={})
    for col in to_create_from:
        for r, g, b in col:
            to_return['red'][r] = 1 + to_return['red'].get(r, 0)
            to_return['green'][g] = 1 + to_return['green'].get(g, 0)
            to_return['blue'][b] = 1 + to_return['blue'].get(b, 0)
    return to_return
