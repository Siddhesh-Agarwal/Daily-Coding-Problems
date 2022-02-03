"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

from random import uniform


def main():
    INTERVAL = 1000
    points_inside_circle = 0
    total_points = 0

    for _ in range(INTERVAL ** 2):
        random_x = uniform(-1, 1)
        random_y = uniform(-1, 1)

        distance_from_origin = random_x ** 2 + random_y ** 2

        if distance_from_origin <= 1:
            points_inside_circle += 1

        total_points += 1
    return round(4 * points_inside_circle / total_points, 3)


if __name__ == "__main__":
    pi = main()
    print(
        f"Final Estimation of π = {pi}"
    )  # Can give different values on every execution
