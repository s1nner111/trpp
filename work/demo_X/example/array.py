def main():
    while True:
        try:
            size = int(input("Введите размер массива (не более 15): "))
            if 1 <= size <= 15:
                break
            else:
                print("Ошибка: размер должен быть от 1 до 15.")
        except ValueError:
            print("Ошибка: введите целое число.")

    print("Введите элементы массива через пробел:")
    while True:
        try:
            numbers = list(map(int, input().split()))
            if len(numbers) == size:
                break
            else:
                print(f"Ошибка: введите ровно {size} чисел.")
        except ValueError:
            print("Ошибка: введите только целые числа.")

    print("\nВведённый массив:")
    print(numbers)


if name == "__main__":
    main()
