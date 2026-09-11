def check_word():
    w = input("Enter a word: ").strip()
    if not w:
        print("Error: empty input")
        return
    if w.istitle():
        print("Could be a proper name (person, city, etc.)")
    else:
        print("Common word")


def main():
    while True:
        print("\n=== MENU (Task 2) ===")
        print("1. Check word")
        print("0. Exit")
        choice = input("Choice: ")
        if choice == "1":
            check_word()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()