import unittest
import tests_12_1 as ts_1
import tests_12_2 as ts_2


myTS = unittest.TestSuite()
myTS.addTest(unittest.TestLoader().loadTestsFromTestCase(ts_1.RunnerTest))
myTS.addTest(unittest.TestLoader().loadTestsFromTestCase(ts_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(myTS)
