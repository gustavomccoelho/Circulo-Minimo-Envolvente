from math import sqrt
import numpy as np
import random
import matplotlib.pyplot as plt
import time

class MinCircle:

    def __init__(self, P):
        self.P = P

    def HeuristicMinCircle(P):

        # Finding Px_max, Px_min, Py_max, Py_min
        X_max = max([abs(x) for x, y in P])
        X_max = [[x, y] for x, y in P if abs(x) == X_max][0]
        X_min = min([abs(x) for x, y in P])
        X_min = [[x, y] for x, y in P if abs(x) == X_min][0]
        Y_max = max([abs(y) for x, y in P])
        Y_max = [[x, y] for x, y in P if abs(y) == Y_max][0]
        Y_min = min([abs(y) for x, y in P])
        Y_min = [[x, y] for x, y in P if abs(y) == Y_min][0]
        points = [X_max, X_min, Y_max, Y_min]

        # Finding the pair with maximum distance
        d_max = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                if d > d_max:
                    d_max = d
                    Pi = points[i]
                    Pj = points[j]

        C = [[0, 0], 0]
        C[0] = [(Pi[0] + Pj[0]) / 2, (Pi[1] + Pj[1]) / 2]
        C[1] = d_max / 2
        for point in P:
            d_mod = sqrt((point[0] - C[0][0]) ** 2 + (point[1] - C[0][1]) ** 2)
            if d_mod > C[1]:
                d_norm = [(point[0] - C[0][0]) / d_mod, (point[1] - C[0][1]) / d_mod]
                C[0][0] = C[0][0] + ((d_mod - C[1]) / 2) * d_norm[0]
                C[0][1] = C[0][1] + ((d_mod - C[1]) / 2) * d_norm[1]
                C[1] = (d_mod + C[1]) / 2

        return C

    def RandomPermutation(A):
        for k in range(len(A) - 1, 0, -1):
            r = random.randrange(0, k)
            temp = A[k]
            A[k] = A[r]
            A[r] = temp
        return A

    def MinCircleWith2Points(P, q1, q2):
        C = [[0.0, 0.0], 0.0]
        C[0][0] = (q1[0] + q2[0]) / 2
        C[0][1] = (q1[1] + q2[1]) / 2
        C[1] = (sqrt((q2[0] - q1[0]) ** 2 + (q2[1] - q1[1]) ** 2)) / 2
        for i in range(0, len(P)):
            d = sqrt((C[0][0] - P[i][0]) ** 2 + (C[0][1] - P[i][1]) ** 2)
            if d > C[1]:
                D = 2 * ((q2[0] - q1[0]) * (P[i][1] - q1[1]) - (P[i][0] - q1[0]) * (q2[1] - q1[1]))
                Cx = ((P[i][1] - q1[1]) * (q2[0] ** 2 + q2[1] ** 2 - q1[0] ** 2 - q1[1] ** 2) - (q2[1] - q1[1]) * (
                            P[i][0] ** 2 + P[i][1] ** 2 - q1[0] ** 2 - q1[1] ** 2)) / D
                Cy = ((q2[0] - q1[0]) * (P[i][0] ** 2 + P[i][1] ** 2 - q1[0] ** 2 - q1[1] ** 2) - (P[i][0] - q1[0]) * (
                            q2[0] ** 2 + q2[1] ** 2 - q1[0] ** 2 - q1[1] ** 2)) / D
                C[0] = [Cx, Cy]
                C[1] = sqrt((q1[0] - C[0][0]) ** 2 + (q1[1] - C[0][1]) ** 2)
        return C

    def MinCircleWithPoint(P, q):
        C = [[0.0, 0.0], 0.0]
        C[0][0] = (P[0][0] + q[0]) / 2
        C[0][1] = (P[0][1] + q[1]) / 2
        C[1] = (sqrt((P[0][0] - q[0]) ** 2 + (P[0][1] - q[1]) ** 2)) / 2
        for i in range(1, len(P)):
            d = sqrt((C[0][0] - P[i][0]) ** 2 + (C[0][1] - P[i][1]) ** 2)
            if d > C[1]:
                C = MinCircle.MinCircleWith2Points(P[0:i], P[i], q)
        return C

    def MinCircle(P):
        P = MinCircle.RandomPermutation(P)
        C = [[0.0, 0.0], 0.0]
        C[0][0] = (P[0][0] + P[1][0]) / 2
        C[0][1] = (P[0][1] + P[1][1]) / 2
        C[1] = (sqrt((P[1][0] - P[0][0]) ** 2 + (P[1][1] - P[0][1]) ** 2)) / 2
        for i in range(2, len(P)):
            d = sqrt((C[0][0] - P[i][0]) ** 2 + (C[0][1] - P[i][1]) ** 2)
            if d > C[1]:
                C = MinCircle.MinCircleWithPoint(P[0:i], P[i])
        return C


if __name__ == '__main__':

    sizes = [10, 100, 1000, 10000, 1000000]
    ex_time_heur = []
    ex_time = []

    for N in sizes:

        # Generatig random values for x and y
        x = np.random.standard_normal(N)
        y = np.random.standard_normal(N)

        # Assigning values to the points
        P = []
        for i in range(N):
            P.append([x[i], y[i]])

        start = time.time()
        C = MinCircle.MinCircle(P)
        end = time.time()
        ex_time.append(end - start)

        start = time.time()
        C_heur = MinCircle.HeuristicMinCircle(P)
        end = time.time()
        ex_time_heur.append(end - start)

        print("MinCircle Center/Radius: " + str(C[0]) + " / " + str(C[1]))
        print("Heuristic Center/Radius: " + str(C_heur[0]) + " / " + str(C_heur[1]))

        # Ploting results

        circle1 = plt.Circle(C[0], C[1], color="r", clip_on=False, fill=False)
        circle2 = plt.Circle(C_heur[0], C_heur[1], color="r", clip_on=False, fill=False)
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.set_title('MinCircle, size = ' + str(N))
        ax1.set_aspect(1)
        ax1.scatter(x, y)
        ax1.set_xlim((-8, 8))
        ax1.set_ylim((-8, 8))
        ax1.add_artist(circle1)
        ax1.plot(C[0][0], C[0][1], 'x', color="r")

        ax2.set_title('Heuristc, size = ' + str(N))
        ax2.set_aspect(1)
        ax2.scatter(x, y)
        ax2.set_xlim((-8, 8))
        ax2.set_ylim((-8, 8))
        ax2.add_artist(circle2)
        ax2.plot(C[0][0], C[0][1], 'x', color="r")
        plt.show()

    # Ploting runtimes

    plt.plot(sizes, ex_time, "r")
    plt.plot(sizes, ex_time_heur, "b")
    plt.xlabel('Input size')
    plt.ylabel('time (s)')
    plt.legend(["MinCircle", "Heuristic"])
    plt.grid(True)
    plt.show()

    # Testing on point.txt

    data = np.loadtxt("points.txt", delimiter="   ")
    C = MinCircle.MinCircle(data)
    C_heur = MinCircle.HeuristicMinCircle(data)
    print("MinCircle Center/Radius: " + str(C[0]) + " / " + str(C[1]))
    print("Heuristic Center/Radius: " + str(C_heur[0]) + " / " + str(C_heur[1]))

    # Ploting results

    circle1 = plt.Circle(C[0], C[1], color="r", clip_on=False, fill=False)
    circle2 = plt.Circle(C_heur[0], C_heur[1], color="r", clip_on=False, fill=False)
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.set_title('MinCircle, points.txt')
    ax1.set_aspect(1)
    ax1.scatter(data[:, 0], data[:, 1])
    ax1.set_xlim((0, 800))
    ax1.set_ylim((0, 800))
    ax1.add_artist(circle1)
    ax1.plot(C[0][0], C[0][1], 'x', color="r")

    ax2.set_title('Heuristc, points.txt')
    ax2.set_aspect(1)
    ax2.scatter(data[:, 0], data[:, 1])
    ax2.set_xlim((0, 800))
    ax2.set_ylim((0, 800))
    ax2.add_artist(circle2)
    ax2.plot(C[0][0], C[0][1], 'x', color="r")
    plt.show()