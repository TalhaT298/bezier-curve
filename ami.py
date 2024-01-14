import matplotlib.pyplot as plt

def factorial(n):
    if n:
        return n * factorial(n - 1)
    else:
        return 1
    
def nCr(n, r):
    return factorial(n) / float(factorial(r) * factorial(n - r))

def BEZ(k, n, u):
    return nCr(n, k) * (u ** k) * ((1 - u) ** (n - k))

def bezierCurve(x_control_points, y_control_points):
    n = len(x_control_points) - 1
    eps = 0.01
    x_curve_points = []
    y_curve_points = []
    u = 0

    while u < 1.01:
        x, y = 0, 0
        for k in range(0, len(x_control_points)):
            bez = BEZ(k, n, u)
            x += x_control_points[k] * bez
            y += y_control_points[k] * bez
        x_curve_points.append(x)
        y_curve_points.append(y)
        u += eps

        plt.clf()
        plt.title("Bezier Curve")
        plt.plot(x_control_points, y_control_points, label = "Control Graph")
        plt.plot(x_curve_points, y_curve_points, label = "Bezier Curve")
        plt.legend()
        plt.grid()
        plt.pause(0.001)

    plt.show()

def main():
    x_control_points = [1, 7, 15, 21]
    y_control_points = [5, 10, 5, 10]

    bezierCurve(x_control_points, y_control_points)
    
if __name__ == "__main__":
    main()