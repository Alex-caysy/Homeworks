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

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        password_h = hash(password)
        user_obj = User(nickname, password_h, age)
        self.users.append(user_obj)
        self.current_user = user_obj.nickname
        print(f'Пользователь {nickname} успешно создан и вошёл в систему')

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user.nickname
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
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age > 18:  # здесь возникает ошибка
                    for i in range(1, video.duration):
                        print(f'{i} ', end='')
                    print('Конец видео')
        return

    def add(self, *args):
        for video in args:
            if video.title not in self.videos:
                self.videos.append(video)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
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
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('vasya_pupkin', 'lolkekcheburek')


print(f'current_user: {ur.current_user}')
# print(f'videos {UrTube.videos}')
