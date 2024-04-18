# написати функцію що отримає речення та виведе його слова у зворотньому порядку
# Речення "Hello people, hello world!"

def reverse_words_in_sentence(sentence: str) -> str:
    cleaned_sentence = sentence.replace(" , ", " ").replace(" ! ", ' ')
    words_list = cleaned_sentence.split()
    print(words_list[::3])

# Розділити речення на окремі слова
# прибрати знаки
# налаштувати зворотній порядок слів
# Зробити першу букву речення великою


 