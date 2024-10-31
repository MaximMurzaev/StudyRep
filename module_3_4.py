
def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word in word:
            same_words.append(word)
    return same_words

result = single_root_words('кол', 'колокол', "сабля", "ледокол", "калькулятор")
result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)
print(result_1)
