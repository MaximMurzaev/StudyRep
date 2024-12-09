import re

class WordsFinder:
    file_names = []
    def __init__(self, *filenames):
        for i in filenames:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file.readlines():
                    words_in_line = re.split(r'[,.=!?;: ]+', line.rstrip())
                    #line.split([',', '.', '=', '!', '?', ';', ':', ' - '])
                    for word in words_in_line:
                        if word not in ['', '-']:
                            words.append(word.lower())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            for word_in_list in words:
                if word_in_list == word.lower():
                    result[name] = words.index(word_in_list) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for name, words in all_words.items():
            words_count = 0
            for word_in_list in words:
                if word_in_list == word.lower():
                    words_count += 1
            if words_count > 0:
                result[name] = words_count
        return result

finder2 = WordsFinder('test_file.txt', 'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))
