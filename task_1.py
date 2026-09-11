import math


def calculate():
    while True:
        try:
            x = float(input("Enter x: "))
        except ValueError as e:
            print(f"Error: {e}")
            continue

        if x <= 0:
            print("Error: x must be greater than 0")
            continue

        try:
            numerator = math.exp(-x) - 4 * x - math.log(x) ** 3
            denominator = math.log10(x + 1) + 1 / math.tan(x ** 2 - 1)
            result = numerator / denominator
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        print(f"y = {result}")
        break


def main():
    while True:
        print("\n=== MENU (Task 1) ===")
        print("1. Calculate y")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            calculate()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()