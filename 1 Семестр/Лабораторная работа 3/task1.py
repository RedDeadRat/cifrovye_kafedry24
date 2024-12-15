# TODO Напишите функцию для поиска индекса товара

def index_finder3000(sought_item):
    if not sought_item in items_list:   #Если товара нет в списке, то и нечего искать его индекс
        return None
    for index, item in enumerate(items_list):
        if item == sought_item:
            return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_finder3000(find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
