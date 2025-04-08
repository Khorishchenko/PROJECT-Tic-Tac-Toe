from random import randrange

def display_board(board):
        separator = '-' * 25
        print('+-------+-------+-------+')
        for i in range(3):
            print('|       |       |       |')
            print(f'|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |')
            print('|       |       |       |')
            print('+-------+-------+-------+')
        print(separator)



def enter_move(board):
    # Функція приймає поточний статус дошки, запитує користувача про його хід,
    # перевіряє введення та оновлює дошку відповідно до рішення користувача.
    value = input("Введіть свій хід: ")
    for i in range(3):
        for j in range(3):
            if board[i][j] == value:
                board[i][j] = 'O'
    display_board(board)




def make_list_of_free_fields(board):
    # Функція перевіряє дошку та створює список усіх вільних квадратів;
    # список складається з кортежів, так що кожен кортеж є парою номерів рядка і стовпчика.
    free_fields = []
    valid_values = {'1', '2', '3', '4', '6', '7', '8', '9'}
    for i in range(3):
        for j in range(3):
            if board[i][j] in valid_values:
                free_fields.append((i, j))
    return free_fields




def winner_for(board, sign):
    # Функція аналізує стан дошки, щоб перевірити, чи
    # э в грі переможець
   # Проверка рядов и столбцов
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    # Проверка диагоналей
    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False



def check_winner(board, player):
    # Функція перевіряє, чи є переможець на дошці для заданого гравця.
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # ряд 1
        [(1, 0), (1, 1), (1, 2)],  # ряд 2
        [(2, 0), (2, 1), (2, 2)],  # ряд 3
        [(0, 0), (1, 0), (2, 0)],  # стовпець 1
        [(0, 1), (1, 1), (2, 1)],  # стовпець 2
        [(0, 2), (1, 2), (2, 2)],  # стовпець 3
        [(0, 0), (1, 1), (2, 2)],  # діагональ 1
        [(0, 2), (1, 1), (2, 0)],  # діагональ 2
    ]
    
    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False


# модифікована функцію draw_move, щоб вона не тільки робила хід комп'ютера, але й блокувала можливість виграшу іншого гравця
def draw_move(board):
    # Функція малює хід комп'ютера та оновлює дошку.
    free_fields = make_list_of_free_fields(board)

    # Спочатку перевіряємо, чи потрібно заблокувати виграш супротивника.
    for x, y in free_fields:
        board[x][y] = 'O'  # Припустимо, що 'O' - це гравець
        if check_winner(board, 'O'):
            board[x][y] = 'X'  # Блокуємо виграш супротивника
            return
        board[x][y] = str(x * 3 + y + 1)  # Повертаємо назад вільне поле
    
    # Якщо немає потреби блокувати, робимо випадковий хід.
    if free_fields:
        x, y = free_fields[randrange(len(free_fields))]
        board[x][y] = 'X'
    else:
        print('No possible moves left. It\'s a draw!')


def main():
    # Основна функція для гри
    board = [['1', '2', '3'],
            ['4', 'X', '6'],
            ['7', '8', '9']]
    print("Welcome to Tic Tac Toe!")
    display_board(board)
    while True:
        # Цикл для гри
        if len(make_list_of_free_fields(board)) != 0:
            enter_move(board)
        else:
            print('It\'s a draw!')
            break
        if winner_for(board, 'X'):
            print('Player X wins!')
            break
        if winner_for(board, 'O'):
            print('Player O wins!')
            break
            
        draw_move(board)
        display_board(board)
        



if __name__ == "__main__":
    main()