import runner_and_tournament as runner
import unittest

class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner.Runner('Усэйн', 10)
        self.runner_2 = runner.Runner('Андрей', 9)
        self.runner_3 = runner.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i in range(len(cls.all_results)):
            print(cls.all_results[i])

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_1(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_3)
        all_results = tournament.start()
        self.assertTrue(all_results[len(all_results)], 'Ник')

        # для того, чтобы выводилось как указано в задании
        i = len(self.all_results)
        self.all_results.update({i: {key : all_results[key].name for key in all_results}})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_2(self):
        tournament = runner.Tournament(90, self.runner_2, self.runner_3)
        all_results = tournament.start()
        self.assertTrue(all_results[len(all_results)], 'Ник')

         # для того, чтобы выводилось как указано в задании
        i = len(self.all_results)
        self.all_results.update({i: {key : all_results[key].name for key in all_results}})

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament_3(self):
        tournament = runner.Tournament(90, self.runner_1, self.runner_3, self.runner_2)
        all_results = tournament.start()
        self.assertTrue(all_results[len(all_results)], 'Ник')

         # для того, чтобы выводилось как указано в задании
        i = len(self.all_results)
        self.all_results.update({i: {key : all_results[key].name for key in all_results}})

if __name__ == 'main':
    unittest.main()
