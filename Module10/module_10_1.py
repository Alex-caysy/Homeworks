import time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = time.time()
time_run = time_end - time_start
print(f'Работа потоков: {time_run}')

thread1 = threading.Thread(target=write_words, args=(10, 'exemple5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'exemple6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'exemple7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'exemple8.txt'))

time_start = time.time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
time_end = time.time()
time_run = time_end - time_start
print(f'Работа потоков: {time_run}')
