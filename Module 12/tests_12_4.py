import unittest
import logging
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='UTF-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        """
        Test for walk function in runner
        :return:
        """
        try:
            obj_walk = rt_with_exceptions.Runner('walk', speed=-2)
            for _ in range(10):
                obj_walk.walk()
            self.assertEqual(obj_walk.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для Runner.', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        """
        Test for run function in runner
        :return:
        """
        try:
            obj_runner = rt_with_exceptions.Runner(2)
            for _ in range(10):
                obj_runner.run()
            self.assertEqual(obj_runner.distance, 100)
            logging.info(f'test_run" выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner.', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        """
        Test for challenge function in runner
        :return:
        """
        runner_obj = rt_with_exceptions.Runner('run')
        walk_obj = rt_with_exceptions.Runner('walk')
        for _ in range(10):
            runner_obj.run()
            walk_obj.walk()
        self.assertNotEqual(runner_obj.distance, walk_obj.distance)


if __name__ == '__main__':

    unittest.main()
