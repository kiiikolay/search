import re
from dict import lists

naming = [
    "clients_field_of_activity",
    "banking_products_for_businesses",
    "clients_profile_picture",
    "summing_up_the_results_and_agreements",
    "clients_objections",
    "products_in_other_banks",
    "information_about_doing_business"
]

def split_text_by_time(text) -> list:
    """
    Разделяет текст на фрагменты по времени.

    Args:
        text: Исходный текст.

    Returns:
        Список строк, где каждая строка - фрагмент текста,
        начавшийся с отметки времени.
    """
    pattern = re.compile(r'(\d{2}:\d{2}:\d{2})')
    parts = []
    current_part = ""
    for line in text.splitlines():
        if pattern.match(line):
            if current_part:
                parts.append(current_part.strip())
            current_part = line
        else:
            current_part += "\n" + line
    if current_part:
        parts.append(current_part.strip())
    return parts

def search(part, words_dict):
    """
    производит поиск ключевых слов в частях текста.

    Args:
        part: часть текста.
        words_dict: список с ключевыпи словами.

    Returns:
        Список строк, где были обнаружены ключевые слова
    """
    result = []
    for pattern in part:
        for patt in words_dict:
            if patt.lower() in pattern.lower():
                result.append(pattern)
    return result



with open("/path/", "r") as dialogue:
    data = dialogue.read()
    part = split_text_by_time(data)
    counter = 0

    for i in lists:
        result = search(part, i)

        with open(f"{naming[counter]}.txt", "a") as log:
            for res in result:
                log.write(res+"\n")

        counter += 1











