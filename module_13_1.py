import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        person_walk = runner.Runner('Person')
        for i in range(10):
            person_walk.walk()
        self.assertEqual(person_walk.distance, 50)

    def test_run(self):
        person_run = runner.Runner('Person')
        for i in range(10):
            person_run.run()
        self.assertEqual(person_run.distance, 100)

    def test_challenge(self):
        person_walk = runner.Runner('Person')
        person_run = runner.Runner('Person')
        for i in range(10):
            person_run.run()
            person_walk.walk()
        self.assertNotEqual(person_run.distance, person_walk.distance)

if __name__ == 'main':
    unittest.main()
