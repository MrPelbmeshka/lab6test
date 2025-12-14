# lab2.py - вторая лабораторная работа
def find_max(numbers):
    """Нахождение максимального числа"""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def main():
    """Основная функция"""
    numbers = [3, 7, 2, 9, 5]
    result = find_max(numbers)
    print(f"Максимальное число в списке {numbers} равно {result}")
    
if __name__ == "__main__":
    main()