import runner as runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
            person_walk = runner.Runner('Person')
            for i in range(10):
                person_walk.walk()
            self.assertEqual(person_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        person_run = runner.Runner('Person')
        for i in range(10):
            person_run.run()
        self.assertEqual(person_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        person_walk = runner.Runner('Person')
        person_run = runner.Runner('Person')
        for i in range(10):
            person_run.run()
            person_walk.walk()
        self.assertNotEqual(person_run.distance, person_walk.distance)

if __name__ == 'main':
    unittest.main()
