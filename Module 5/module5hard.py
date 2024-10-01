import time

class User:
    def __init__(self, nickname, password, age):
        self.user = {}
        self.nickname = nickname
        self.password = password
        self.age = age
        # self.user[nickname] = [password, age]


class Video:
    def __init__(self,  title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def current_user(self):
        print(f'current user ')

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        password_h = hash(password)
        user_obj = User(nickname, password_h, age)
        self.users.append(user_obj)
        self.current_user = user_obj
        print(f'Пользователь {nickname} успешно создан и вошёл в систему')

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                print(f'Пользователь {nickname} вошёл в систему')
                return
        print(f'Неверный логин или пароль')

    def log_out(self):
        self.current_user = None

    def get_videos(self, search_phrase):
        answer_list = []
        for video in self.videos:
            if search_phrase.lower() in video.title.lower():
                answer_list.append(video.title)
        return answer_list

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Видео доступно только для пользователей старше 18 лет')
                    return
                for i in range(1, video.duration + 1):
                    #time.sleep(1)
                    video.time_now = i
                    print(f'{video.time_now} ', end='')
                print('Конец видео')
        return

    def add(self, *args):
        for video in args:
            if video.title not in self.videos:
                self.videos.append(video)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.log_in('vasya_pupkin', 'lolkekcheburek')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

print(ur.current_user)
