import threading
import time

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        pass
    with open(file_name, 'a', encoding='utf8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {str(i)}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time.time()
print(f'Время работы функций {end_time - start_time}')

start_time_thread = time.time()
thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt')).start()
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt')).start()
thread_3= threading.Thread(target=write_words, args=(200, 'example7.txt')).start()
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt')).start()
while threading.active_count() > 1:
    pass
end_time_thread = time.time()
print(f'Время работы потоков {end_time_thread - start_time_thread}')

