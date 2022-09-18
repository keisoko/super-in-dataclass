"""
Fork of  the Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with __post_init__, and Enum 
"""

import random
import string
from dataclasses import dataclass, field
from enum import Enum


@dataclass(frozen=True)
class ConstantNamespace:
    PAY_RAISE_RATE = 1.04


constant = ConstantNamespace()


def generate_id(length: int):
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))


class Role(Enum):
    """Employee roles."""

    WORKER = "Worker"
    MANAGER = "Manager"
    INTERN = "Intern"


@dataclass(slots=True, kw_only=True, order=True)
class Employee:
    """Employee parent class."""

    person_name: str
    person_age: int
    employee_pay_amount: int
    employee_role: Role
    employee_id: str = field(init=False)
    employee_email: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the employee's id."""
        self.employee_id = generate_id(length=8)
        first_name, last_name = self.person_name.split()
        self.employee_email = f"{first_name.lower()}.{last_name.lower()}@company.com"

    @property
    def apply_raise(self) -> None:
        """Applies the company raise rate to the employee's payment amount"""
        self.employee_pay_amount = int(
            self.employee_pay_amount * constant.PAY_RAISE_RATE
        )

    @property
    def say_email(self) -> str:
        """Returns the email address"""
        return f"My email address is {self.employee_email}"

    @property
    def say_pay_amount(self) -> str:
        """Returns the employee's pay amount"""
        return f"My pay is ${self.employee_pay_amount:_}."

    @property
    def say_description(self) -> str:
        """Displays the employee's description"""
        return f"My name is {self.person_name} and I am a {self.person_age} years old."


@dataclass
class Worker(Employee):
    """Worker class"""

    @property
    def say_worker_id_role(self) -> str:
        """Returns the worker id and role"""
        return f"My id is {self.employee_id} and I am a {self.employee_role.value}."


@dataclass
class Intern(Employee):
    """Intern class"""

    @property
    def say_intern_id_and_role(self) -> str:
        """Returns the intern id and role"""
        return f"My id is {self.employee_id} and I am an {self.employee_role.value}."


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    managed_employees: list[str] = field(default_factory=list)

    def add_employee(self, new_employee) -> None:
        """Add a new employee to the managed_employees list."""
        if new_employee not in self.managed_employees:
            self.managed_employees.append(new_employee)

    @property
    def say_manager_id_and_role(self) -> str:
        """Returns the manager id and role"""
        return f"My id is {self.employee_id} and I am a {self.employee_role.value}."

    @property
    def say_supervised_employees(self) -> str:
        """Returns employees that are supervised by the manger"""
        return f"The employees under my supervision are {self.managed_employees}."


worker1 = Worker(
    person_name="Mary Smith",
    person_age=30,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
worker2 = Worker(
    person_name="John Doe",
    person_age=35,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
worker3 = Worker(
    person_name="Alexander Octavian",
    person_age=27,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
intern1 = Intern(
    person_name="Jennifer Ivans",
    person_age=20,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
intern2 = Intern(
    person_name="Brian Donahue",
    person_age=19,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
intern3 = Intern(
    person_name="Bernard Johnson",
    person_age=22,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
manager1 = Manager(
    person_name="Brandon Smith",
    person_age=40,
    employee_pay_amount=90_000,
    managed_employees=[worker1.person_name, worker2.person_name],
    employee_role=Role.MANAGER,
)
manager2 = Manager(
    person_name="Markus Sextus",
    person_age=45,
    employee_pay_amount=90_000,
    managed_employees=[intern1.person_name, intern2.person_name],
    employee_role=Role.MANAGER,
)


def execute_main() -> None:

    workers = [worker1, worker2, worker3]
    sorted_workers = sorted(workers, key=lambda worker: worker.person_age)

    for worker in sorted_workers:
        worker.apply_raise
        print(worker.say_description)
        print(worker.say_email)
        print(worker.say_pay_amount)
        print(worker.say_worker_id_role, "\n")

    print()

    interns = [intern1, intern2, intern3]
    sorted_interns = sorted(interns, key=lambda intern: intern.person_age)

    for intern in sorted_interns:
        intern.apply_raise
        print(intern.say_description)
        print(intern.say_email)
        print(intern.say_pay_amount)
        print(intern.say_intern_id_and_role, "\n")

    print()

    manager1.add_employee(worker3.person_name)
    manager2.add_employee(intern3.person_name)

    managers = [manager1, manager2]

    for manager in managers:
        manager.apply_raise
        print(manager.say_description)
        print(manager.say_email)
        print(manager.say_pay_amount)
        print(manager.say_manager_id_and_role)
        print(manager.say_supervised_employees, "\n")


if __name__ == "__main__":
    execute_main()
