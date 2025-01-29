import logging
import rt_with_exceptions as runner

class RunnerTest:

    def test_walk(self):
        try:
            person_walk = runner.Runner('Person', )
            for i in range(10):
                person_walk.walk()
            logging.info('"test_walk" выполнен успешно')
        except TypeError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            person_run = runner.Runner('Person', -5)
            for i in range(10):
                person_run.run()
            logging.info('"test_run" выполнен успешно')
        except ValueError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        person_walk = runner.Runner('Person')
        person_run = runner.Runner('Person')
        for i in range(10):
            person_run.run()
            person_walk.walk()

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(levelname)s | %(message)s')
runner_test = RunnerTest()
runner_test.test_walk()
runner_test.test_run()


