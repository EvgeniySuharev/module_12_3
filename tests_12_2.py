import code_for_test_2 as code
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.Usein = code.Runner('Усейн', speed=10)
        self.Andrey = code.Runner('Андрей', speed=9)
        self.Nik = code.Runner('Ник', speed=3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        test_tournament = code.Tournament(90,
                                          self.Usein, self.Nik)
        res = test_tournament.start()
        self.all_results['Усейн и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        test_tournament = code.Tournament(90,
                                          self.Andrey, self.Nik)
        res = test_tournament.start()
        self.all_results['Андрей и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        test_tournament = code.Tournament(90,
                                          self.Usein, self.Andrey, self.Nik)
        res = test_tournament.start()
        self.all_results['Усейн, Андрей и Ник'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Nik)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_4(self):
        """
        доп тест на логическую ошибку
        :return:
        """
        test_tournament = code.Tournament(9,
                                          self.Andrey, self.Usein)
        res = test_tournament.start()
        self.all_results['Андрей - Усейн'] = res
        key = max(res.keys())
        self.assertTrue(res[key] == self.Andrey)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            print(key)
            for i in cls.all_results[key]:
                print(f'{cls.all_results[key][i]} - {i}')
            print()


if __name__ == '__main__':
    unittest.main()
