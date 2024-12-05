import  time
from random import randint

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
        if self.current_user is None:
            print('Пользователь с таким именем и паролем не найден')

    def register(self, nickname, password, password_confirm, age):
        if password == password_confirm:
            user_not_found = True
            for user in self.users:
                if nickname == user.nickname:
                    print('Пользователь с таким именем существует. Задайте новое имя пользователя')
                    break
            if user_not_found:
                user = User(nickname, password, age)
                self.users.append(user)
                self.current_user = user
                print(f'Пользователь {nickname} добавлен!')

    def log_out(self):
        self.current_user = None

    def __add__(self, other):
        video_not_found = True
        for video in self.videos:
            if video.title == other.title:
                video_not_found = False
                break
        if video_not_found:
            self.videos.append(other)
            print('Видео успешно добавлено!')
        else:
            print('Это видео уже загружено')

    def get_videos(self, find_word):
        found_videos = []
        for video in self.videos:
            if find_word.lower() in video.title.lower():
                found_videos.append(video.title)
        if len(found_videos) > 0:
            print(f'По поисковому запросу{find_word} найдены следующие видео:\n')
            for i in range(len(found_videos)):
                print(f'{i + 1}. {found_videos[i]}')

    def watch_video(self, watch_title):
        for video in self.videos:
            if watch_title.lower() == video.title.lower():
                if self.current_user is not None:
                    if video.adult and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(video.duration):
                            print(i)
                            time.sleep(1)
                            video.time_now = i
                        print('Конец видео')
                        video.time_now = 0
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                break

class Video:
    def __init__(self, title, duration = 0, adult = False):
        self.title = title
        self.duration = randint(10, 200)
        self.adult = adult
        self.time_now = 0


class User:
    def __init__(self, nickname, password, age):
        self.password = hash(password)
        self.nickname = nickname
        self.age = age

if __name__ == '__main__':
    urtube = UrTube()
    print('Приветствуем вас в видео портале!')
    while True:
        print('-----------Меню команд:---------\n'
              '1. Зарегистрировать пользователя\n'
              '2. Авторизоваться\n'
              '3. Добавить видео\n'
              '4. Найти видео по наименованию\n'
              '5. Просмотр видео\n'
              '6. Авторизованный пользователь\n'
              '7. Разлогиниться\n'
              '0. Выход\n')
        choice = input('Введите команду: ')
        if choice == '1':
            urtube.register(input(f'Введите имя пользователя: '),
                            pass_word := input(f'Введите пароль: '),
                            pass_conf := input(f'Введите подтверждение пароля: '),
                            int(input(f'Введите свой возраст: ')))
            if pass_word != pass_conf:
                print('Пароль и подтверждение не совпадают! Невозможно добавить пользователя')
                continue
        elif choice == '2':
            urtube.log_in(input(f'Введите имя пользователя: '),
                            pass_word := input(f'Введите пароль : '))
        elif choice == '3':
            title = input('Введите название видео: ')
            adult = int(input('Нужен возрастной контроль(18+). Введите 1 если нужен. 0 если не нужен: '))
            print(adult)
            video = Video(title=title, adult=bool(adult))
            urtube.__add__(video)
        elif choice == '4':
            urtube.get_videos(input('Введите название фильма для поиска: '))
        elif choice == '5':
            urtube.watch_video(input('Введите название фильма для просмотра: '))
        elif choice == '6':
            print(urtube.current_user.nickname)
        elif choice == '7':
            urtube.log_out()
        elif choice == '0':
            urtube.log_out()
            break
        else:
            print('Такой команды нет! Введите правильную команду')

