# lab1.py - первая лабораторная работа
def calculate_sum(numbers):
    """Вычисление суммы чисел"""
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    """Основная функция"""
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    print(f"Сумма чисел {numbers} равна {result}")
    
if __name__ == "__main__":
    main()