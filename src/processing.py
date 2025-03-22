def filter_by_state(my_list: list, state: str = 'EXECUTED') -> list:
    '''Функция отфильтровывает список словарей по ключу'''
    new_list = []
    for dict in my_list:
        for key, value in dict.items():
            if value == state:
                new_list.append(dict)
    return new_list


def sort_by_date(my_list: list, reverse: bool = True) -> list:
    '''Функция сортирует список словарей по дате'''
    sorted_list = sorted(my_list, key=lambda x: x['date'], reverse=reverse)
    return sorted_list


print()
