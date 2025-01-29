import unittest
import runner_test
import tournamement_test

runner_and_tournamentST = unittest.TestSuite()
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.RunnerTest))
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tournamement_test.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_and_tournamentST)