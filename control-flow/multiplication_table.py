def main() -> None:
    try:
        number = int(input("Enter a number to see its multiplication table: ").strip())
    except ValueError:
        print("Invalid number input.")
        return

    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")


if __name__ == "__main__":
    main()


