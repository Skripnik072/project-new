def filter_by_state(my_list: list, state: str = 'EXECUTED') -> list:
    '''Функция отфильтровывает список словарей по ключу'''
    new_list = []
    for dict in my_list:
        for key, value in dict.items():
            if value == state:
                new_list.append(dict)
    return new_list