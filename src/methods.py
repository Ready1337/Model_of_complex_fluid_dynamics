def eulers_example(point, precision):
    x0 = point[0]
    y0 = point[1]

    x = x0 + precision * y0
    y = y0 + precision * (-x0)

    return x, y


def runge_kutta_example(point, precision):
    x0 = point[0]
    y0 = point[1]

    k1 = precision * y0
    l1 = precision * (-x0)

    k2 = precision * (y0 + l1/2)
    l2 = precision * (-x0 - k1/2)

    k3 = precision * (y0 + l2/2)
    l3 = precision * (-x0 - k2/2)

    k4 = precision * (y0 + l3)
    l4 = precision * (-x0 - k3)

    x = x0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    y = y0 + 1/6 * (l1 + 2*l2 + 2*l3 + l4)

    return x, y


def eulers_model(point, precision, param):
    x0 = point[0]
    y0 = point[1]

    x = x0 + precision * y0
    y = y0 + precision * (-(x0**2) + 3*x0 - 2) * y0 - 4*x0 + 4*param

    return x, y


def runge_kutta_model(point, precision, param):
    x0 = point[0]
    y0 = point[1]

    k1 = precision * y0
    l1 = precision * (-(x0**2) + 3*x0 - 2) * y0 - 4*x0 + 4*param

    k2 = precision * (y0 + l1/2)
    l2 = precision * (-((x0 + k1/2)**2) + 3*(x0 + k1/2) - 2) * (y0 + l1/2) - 4*(x0 +k1/2) + 4*param

    k3 = precision * (y0 + l2/2)
    l3 = precision * (-((x0 + k2/2)**2) + 3*(x0 + k2/2) - 2) * (y0 + l2/2) - 4*(x0 +k2/2) + 4*param

    k4 = precision * (y0 + l3)
    l4 = precision * (-((x0 + k3)**2) + 3*(x0 + k3) - 2) * (y0 + l3) - 4*(x0 +k3) + 4*param

    x = x0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    y = y0 + 1/6 * (l1 + 2*l2 + 2*l3 + l4)

    return x, y
