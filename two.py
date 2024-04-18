

def reverse_words_in_sentence(sentence: str) -> str:
    cleaned_sentence = sentence.replace(" , ", " ").replace(" ! ", ' ')
    words_list = cleaned_sentence.split()
    print(words_list[::3])


 