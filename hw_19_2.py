"""
Не знаю что писать. В голове пусто
"""
def plus_two(number):
    """
    выводит результат сложения
    переданного в нее числа
    """
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Ожидаемый тип данных - число!")

if __name__ == "__main__":
    plus_two(3)
    plus_two("3")
