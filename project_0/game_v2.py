import numpy as np

def random_predict(number: int = 1) -> int:
    """_Рандомно заданное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count
print(f"Количество попыток: {random_predict()}")

def score_game(randon_predict) -> int:
    """За какое количество в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        randon_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    np.random.seed(1) # фиксируем сид производительности
    random_array = np.random.randint(1,100, size=(1000)) # загадали спиок чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__== '_main_':
    score_game(random_predict)
    
    