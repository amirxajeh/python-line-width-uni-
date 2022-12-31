import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calculate_distance_from_another_point(self, point):
        return math.sqrt(math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))


if __name__ == '__main__':
    point_counts = int(input("Enter points count: "))

    points = []
    for i in range(point_counts):
        x = float(input("Enter #{} point x: ".format(i + 1)))
        y = float(input("Enter #{} point y: ".format(i + 1)))

        points.append(Point(x, y))

    width = 0
    for i in range(point_counts - 1):
        width += points[i].calculate_distance_from_another_point(points[i + 1])

    print("Line width is {}".format(width))