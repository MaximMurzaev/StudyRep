from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open (name, 'r') as file:
        for line in file:
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
# Линейный вызов
# for filename in filenames:
#     read_info(filename)
# Многопроцессный
if __name__ == '__main__':
    with Pool(4) as p:
        p.map(read_info, filenames)
end_time = time.time()

print(end_time - start_time)

