import time
from multiprocessing import Pool


def read_info(name):
    all_data =[]
    with open(name) as file:
        while True:
            readed_line = file.readline()
            if readed_line == '':
                break
            all_data.append(readed_line)


if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

    time_start = time.time()
    for name in filenames:
        read_info(name)
    time_end = time.time()
    print(time_end - time_start)

    time_start = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = time.time()
    print(time_end - time_start)
