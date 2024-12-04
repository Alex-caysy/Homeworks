import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TournamentTest.all_results = {}

    def setUp(self):
        self.Usain = runner_and_tournament.Runner('Usain', 10)
        self.Andrey = runner_and_tournament.Runner('Andrey', 9)
        self.Nick = runner_and_tournament.Runner('Nick', 3)

    def test_race1(self):
        """
        Test for start function in runner_and_tournament
        :return:
        """
        race1 = runner_and_tournament.Tournament(90, self.Usain, self.Nick)
        TournamentTest.all_results.update({'race1': race1.start()})
        last_runner_id = max(TournamentTest.all_results['race1'])
        last_runner = TournamentTest.all_results['race1'].get(last_runner_id)
        self.assertTrue(last_runner == self.Nick)

    def test_race2(self):
        """
        Test2 for start function in runner_and_tournament
        :return:
        """
        race2 = runner_and_tournament.Tournament(90, self.Andrey, self.Nick)
        TournamentTest.all_results.update({'race2': race2.start()})
        last_runner_id = max(TournamentTest.all_results['race2'])
        last_runner = TournamentTest.all_results['race2'].get(last_runner_id)
        self.assertTrue(last_runner == self.Nick)

    def test_race3(self):
        """
        Test for start function in runner_and_tournament
        :return:
        """
        race3 = runner_and_tournament.Tournament(90, self.Usain, self.Andrey, self.Nick)
        TournamentTest.all_results.update({'race3': race3.start()})
        last_runner_id = max(TournamentTest.all_results['race3'])
        last_runner = TournamentTest.all_results['race3'].get(last_runner_id)
        self.assertTrue(last_runner == self.Nick)

    def test_race4(self):
        """
        Test for start function in runner_and_tournament
        :return:
        """
        race4 = runner_and_tournament.Tournament(3, self.Usain, self.Andrey, self.Nick)
        TournamentTest.all_results.update({'race4': race4.start()})
        last_runner_id = max(TournamentTest.all_results['race4'])
        last_runner = TournamentTest.all_results['race4'].get(last_runner_id)
        self.assertTrue(last_runner == self.Nick)

    @classmethod
    def tearDownClass(cls):
        for value_dict in TournamentTest.all_results.values():
            race = {}
            for key, value in value_dict.items():
                race.update({key: value.name})
            print(race)
