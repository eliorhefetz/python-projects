import unittest

from src.factory import Employee, Factory, Manager


class TestFactory(unittest.TestCase):
    def test_get_best_worker_returns_highest_hours(self):
        factory = Factory("SCE")
        factory.AddWorker(Employee(101, "Elior", 150, 50))
        factory.AddWorker(Employee(102, "Moshe", 170, 50))

        self.assertEqual(factory.GetBestWorker(), (102, "Moshe"))

    def test_promote_increases_salary_for_eligible_workers(self):
        factory = Factory("SCE")
        worker = Employee(101, "Elior", 170, 50)
        factory.AddWorker(worker)

        promoted = factory.Promote()

        self.assertEqual(len(promoted), 1)
        self.assertAlmostEqual(promoted[0][1], 9350.0)

    def test_best_managers_filters_by_rank_and_hours(self):
        factory = Factory("SCE")
        factory.AddWorker(Manager(201, "Boss Ina", 100, 100, 2000, 1))
        factory.AddWorker(Manager(202, "Big Boss", 130, 200, 5000, 3))
        factory.AddWorker(Manager(203, "Team Lead", 165, 80, 1000, 2))

        managers = factory.BestManagers()

        self.assertEqual([manager.name for manager in managers], ["Big Boss", "Team Lead"])


if __name__ == "__main__":
    unittest.main()
