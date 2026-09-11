import math


def task_a():
    print("Task A")
    print("-" * 28)
    x_step = 0.8
    x = 0.2
    print(f"{'x':^10} | {'y':^15}")
    print("-" * 28)
    while x <= 10:
        try:
            y = x + math.cos(2 * x) / (x + 2)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            print(f"{x:^10.2f} | {y:^15.5f}")
        x += x_step


def task_b():
    print("Task B")
    print("-" * 28)
    x_step = 1.5
    x = 0.6
    n = 6
    print(f"{'x':^10} | {'y':^15}")
    print("-" * 28)
    for _ in range(n):
        try:
            y = x + math.cos(2 * x) / (x + 2)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            print(f"{x:^10.2f} | {y:^15.5f}")
        x += x_step


def main():
    while True:
        print("\n=== MENU (Task 3, Variant 5) ===")
        print("1. Task A")
        print("2. Task B")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            task_a()
        elif choice == "2":
            task_b()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()