def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b

def subtract(a, b):
    """Возвращает разность двух чисел."""
    return a - b

def main():
    print("=== Калькулятор ===")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")

if __name__ == "__main__":
    main()
