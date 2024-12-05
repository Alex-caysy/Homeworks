import unittest
import runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        obj_walk = runner.Runner('walk')
        for _ in range(10):
            obj_walk.walk()
        self.assertEqual(obj_walk.distance, 50)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        obj_runner = runner.Runner('run')
        for _ in range(10):
            obj_runner.run()
        self.assertEqual(obj_runner.distance, 100)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        """
        Test for challenge function in runner
        :return:
        """
        runner_obj = runner.Runner('run')
        walk_obj = runner.Runner('walk')
        for _ in range(10):
            runner_obj.run()
            walk_obj.walk()
        self.assertNotEqual(runner_obj.distance, walk_obj.distance)


if __name__ == '__main__':
    unittest.main()
