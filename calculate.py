import math
import random


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def in_circle(self) -> bool:
        return math.sqrt(self.x ** 2 + self.y ** 2) < 1


def calculate(data_point_count) -> float:
    in_circle_count = 0
    for _ in range(data_point_count):
        in_circle_count += Point(x=random.random(), y=random.random()).in_circle()

    return 4 * (in_circle_count / data_point_count)


def main() -> None:
    result = calculate(data_point_count=10000000)
    print(f'Pi prediction: {result}')


if __name__ == '__main__':
    main()
