# TODO Напишите функцию find_common_participants

def find_common_participants(str1, str2, delimiter=','):
    list_participants1 = str1.split(delimiter)
    list_participants2 = str2.split(delimiter)
    intersection_list = list(set(list_participants1).intersection(list_participants2))
    intersection_list.sort()
    return intersection_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(str1=participants_first_group,
                                               str2=participants_second_group,
                                               delimiter='|')
print(common_participants)
# TODO Проверьте работу функции с разделителем отличным от запятой

