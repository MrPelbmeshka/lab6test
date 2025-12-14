# lab1.py - первая лабораторная работа (ИЗМЕНЕННАЯ ВЕРСИЯ В lab2)
def calculate_average(numbers):
    """Вычисление среднего арифметического"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    """Основная функция"""
    numbers = [10, 20, 30, 40, 50]
    result = calculate_average(numbers)
    print(f"Среднее чисел {numbers} равно {result}")
    
if __name__ == "__main__":
    main()