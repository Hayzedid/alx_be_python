def main() -> None:
    try:
        size = int(input("Enter the size of the pattern: "))
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return

    if size <= 0:
        print("Invalid input. Please enter a positive integer.")
        return

    row = 0
    while row < size:
        for _ in range(size):
            print("*", end="")
        print()
        row += 1


if __name__ == "__main__":
    main()
