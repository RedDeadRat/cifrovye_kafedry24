# TODO  Напишите функцию count_letters

def text_formater3000(unformatted_text):
    formatted_text = ""
    for char in unformatted_text.lower():   #Форматируем текст, все буквы приводим к нижнему регистру,
        if char.isalpha():                  #все не буквы - удаляем
            formatted_text+=char
    return formatted_text

def count_letters(unformatted_text):
    formatted_text = text_formater3000(unformatted_text)
    count_dict = {}
    for letter in formatted_text:
        if letter in count_dict:
            count_dict[letter]+=1
        else:
            count_dict[letter]=1
    return count_dict

def calculate_frequency(letters_dict):
    frequency_dict = {}
    for letter_count in letters_dict.items():
        frequency = int(letter_count[1]) / len(text_formater3000(main_str))
        frequency_dict[letter_count[0]] = frequency
    return frequency_dict

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Напишите функцию calculate_frequency
count_letters(main_str)



# TODO Распечатайте в столбик букву и её частоту в тексте
for latter_frequency in calculate_frequency(count_letters(main_str)).items():
    print(f"{latter_frequency[0]}: {latter_frequency[1]:.2f}")