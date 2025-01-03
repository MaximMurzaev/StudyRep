team1_num = 5
team2_num = 6

score_1 = 40
score_2 = 42

team1_time = 1552.512
team2_time = 2153.31451

tasks_total = 82
time_avg = 45.2

challenge_result = 'Победа команды Волшебники данных!'

#Использование %:
print('В команде "Мастера кода" участников: %s!' % 5)
print('Итого сегодня в командах участников: %s и %s!' % (5, 6))
print('Итого сегодня в командах участников: %(num_1)s и %(num_2)s!' % {'num_1' : team1_num, 'num_2' : team2_num})

#Использование format():
print('Команда "Волшебники данных" решила задач: {}!'.format(score_2))
print('"Волшебники данных" решили задачи за {}!'.format(team1_time))
print('Итого сегодня в командах участников: {num_1} и {num_2}!'.format(num_1=team1_num, num_2=team2_num))

#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print(challenge_result)

print(f'Сегодня было решено {score_1 + score_2}, в среднем по {round((team1_time + team2_time) / (score_1 + score_2), 1)} секунды на задачу!')