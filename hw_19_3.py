"""
Не знаю что писать. В голове пусто
"""
def access_array_element(array, index):
    """
    Не знаю что писать. В голове пусто
    """
    try:
        value = array[index]
        print("Значение элемента с индексом", index, ":", value)
    except IndexError:
        print("Ошибка: Индекс выходит за границы массива!")

if __name__ == "__main__":
    my_array = [1, 2, 3, 4, 5]
    access_array_element(my_array, 10) 
    