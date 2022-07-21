"""
Fork of  the Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with __post_init__, and Enum 
"""

import random
import string
from dataclasses import dataclass, field
from enum import Enum

PAY_RAISE_RATE = 1.04


def generate_id(length: int):
    """Helper function to generate id."""
    return "".join(random.choices(string.hexdigits.upper(), k=length))


class Role(Enum):
    """Employee roles."""

    WORKER = "Worker"
    MANAGER = "Manager"
    INTERN = "Intern"


@dataclass(slots=True, kw_only=True)
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
        self.employee_pay_amount = int(self.employee_pay_amount * PAY_RAISE_RATE)

    @property
    def description(self) -> str:
        """Displays the employee's greeting"""
        return f"My name is {self.person_name}, I am a {self.person_age} years old, my email address is {self.employee_email}"


@dataclass
class Worker(Employee):
    """Worker class"""

    @property
    def description(self) -> str:
        """Extends the parent description method."""
        return f"{super().description}. My id is {self.employee_id} and I am a {self.employee_role.value}. My pay is ${self.employee_pay_amount:,}."


@dataclass
class Intern(Employee):
    """Intern class"""

    @property
    def description(self) -> str:
        """Extends the parent description method."""
        return f"{super().description}. My id is {self.employee_id} and I am an {self.employee_role.value}. My pay is ${self.employee_pay_amount:,}."


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    managed_employees: list[str] = field(default_factory=list)

    def add_employee(self, new_employee) -> None:
        """Add a new employee to the managed_employees list."""
        if new_employee not in self.managed_employees:
            self.managed_employees.append(new_employee)

    @property
    def description(self) -> str:
        """Extends the parent description method"""
        return f"{super().description}. My id is {self.employee_id} and I am a {self.employee_role.value}. The employees under my supervision are {self.managed_employees} and my pay is ${self.employee_pay_amount:,}."


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

    worker1.apply_raise
    worker2.apply_raise
    worker3.apply_raise

    workers = [worker1, worker2, worker3]

    for worker in workers:
        print(worker.description)

    print()

    intern1.apply_raise
    intern2.apply_raise
    intern3.apply_raise

    interns = [intern1, intern2, intern3]

    for intern in interns:
        print(intern.description)

    print()

    manager1.apply_raise
    manager2.apply_raise

    manager1.add_employee(worker3.person_name)
    manager2.add_employee(intern3.person_name)

    managers = [manager1, manager2]

    for manager in managers:
        print(manager.description)


if __name__ == "__main__":
    execute_main()
