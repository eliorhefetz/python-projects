from dataclasses import dataclass, field


@dataclass
class Employee:
    emp_id: int
    name: str
    monthly_hours: float
    hourly_rate: float
    monthly_salary: float = field(default=0, init=False)

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if self.emp_id <= 0:
            raise ValueError("Employee ID must be greater than 0.")
        if not self.name:
            raise ValueError("Employee name cannot be empty.")
        if self.monthly_hours < 0:
            raise ValueError("Monthly hours cannot be negative.")
        if self.hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")

    def GetSalary(self) -> float:
        self.monthly_salary = self.monthly_hours * self.hourly_rate
        return self.monthly_salary


@dataclass
class Manager(Employee):
    bonus: float
    rank: int

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.bonus < 0:
            raise ValueError("Bonus cannot be negative.")
        if not 1 <= self.rank <= 3:
            raise ValueError("Rank must be between 1 and 3.")

    def GetSalary(self) -> float:
        base_salary = self.monthly_hours * self.hourly_rate
        self.monthly_salary = (base_salary + self.bonus) * self.rank
        return self.monthly_salary


class Factory:
    def __init__(self, name: str) -> None:
        self.name = name.strip()
        if not self.name:
            raise ValueError("Factory name cannot be empty.")
        self.workers: list[Employee] = []

    def __repr__(self) -> str:
        return f"Factory(name='{self.name}', workers_count={len(self.workers)})"

    def AddWorker(self, worker: Employee) -> None:
        if any(existing_worker.emp_id == worker.emp_id for existing_worker in self.workers):
            raise ValueError(f"Worker with ID {worker.emp_id} already exists.")
        self.workers.append(worker)

    def GetBestWorker(self):
        if not self.workers:
            return None

        best_worker = self.workers[0]
        for worker in self.workers[1:]:
            if worker.monthly_hours > best_worker.monthly_hours:
                best_worker = worker

        return best_worker.emp_id, best_worker.name

    def Promote(self) -> list[tuple[str, float]]:
        promoted_workers: list[tuple[str, float]] = []

        for worker in self.workers:
            if worker.monthly_hours > 160:
                worker.hourly_rate *= 1.10
                new_salary = worker.GetSalary()
                promoted_workers.append((worker.name, new_salary))

        return promoted_workers

    def BestManagers(self) -> list[Manager]:
        qualified_managers: list[Manager] = []

        for worker in self.workers:
            if isinstance(worker, Manager) and worker.rank >= 2 and worker.monthly_hours > 120:
                qualified_managers.append(worker)

        return qualified_managers


def run_factory_examples() -> None:
    my_factory = Factory("SCE")

    emp1 = Employee(101, "Elior", 150, 50)
    emp2 = Employee(102, "Moshe", 170, 50)
    mgr1 = Manager(201, "Boss Ina", 100, 100, 2000, 1)
    mgr2 = Manager(202, "Big Boss", 130, 200, 5000, 3)
    mgr3 = Manager(203, "Team Lead", 165, 80, 1000, 2)

    my_factory.AddWorker(emp1)
    my_factory.AddWorker(emp2)
    my_factory.AddWorker(mgr1)
    my_factory.AddWorker(mgr2)
    my_factory.AddWorker(mgr3)

    print(my_factory)

    for worker in my_factory.workers:
        print(f"{worker.name}: {worker.GetSalary()}")

    print("Best worker:", my_factory.GetBestWorker())
    print("Promoted list:", my_factory.Promote())
    print("Best managers:", my_factory.BestManagers())


if __name__ == "__main__":
    run_factory_examples()
