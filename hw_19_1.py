"""
это уже трети или четврёртый шахмат
"""
class ChessBoard:
    """
    Класс, представляющий шахматную доску.
    """
    def __init__(self):
        """
        Инициализация шахматной доски.
        """
        self.board = [[0] * 8 for _ in range(8)]

    def is_valid_position(self, row, col):
        """
        Проверка, является ли позиция корректной на доске.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def can_queen_move(self, start, end):
        """
        Определение возможности хода ферзя.
        """
        row_start, col_start = start
        row_end, col_end = end

        if abs(row_end - row_start) == abs(col_end - col_start):
            return True

        return row_start == row_end or col_start == col_end

    def can_knight_move(self, start, end):
        """
        Определение возможности хода коня.
        """
        row_start, col_start = start
        row_end, col_end = end

        return (abs(row_end - row_start) == 2 and abs(col_end - col_start) == 1) or \
               (abs(row_end - row_start) == 1 and abs(col_end - col_start) == 2)

if __name__ == "__main__":
    chess_board = ChessBoard()

    try:
        start_pos = tuple(map(int, input("Введите координаты начальной "
                                          "клетки (строка, столбец): ").split()))
        end_pos = tuple(map(int, input("Введите координаты конечной "
                                        "клетки (строка, столбец): ").split()))

        if not chess_board.is_valid_position(*start_pos) or \
            not chess_board.is_valid_position(*end_pos):
            raise ValueError("Некорректные координаты клеток")

        queen_possible = chess_board.can_queen_move(start_pos, end_pos)
        knight_possible = chess_board.can_knight_move(start_pos, end_pos)

        if queen_possible:
            print("Ферзь может попасть на эту клетку одним ходом")
        else:
            print("Ферзь не может попасть на эту клетку одним ходом")

        if knight_possible:
            print("Конь может попасть на эту клетку одним ходом")
        else:
            print("Конь не может попасть на эту клетку одним ходом")

    except ValueError as exc:
        print("Ошибка:", exc)
    except Exception as exc:
        print("Произошла ошибка:", exc)
