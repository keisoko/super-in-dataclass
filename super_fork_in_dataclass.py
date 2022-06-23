"""
Fork of  the Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with __post_init__, and Enum 
"""

import random
import string
from dataclasses import dataclass, field
from enum import Enum


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
    employee_role: Role
    email_address: str = field(init=False)
    employee_id: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the employee's id and email address."""
        first_name, last_name = self.person_name.split(" ")
        self.email_address = f"{first_name}.{last_name}@company.com"
        self.employee_id = generate_id(length=8)

    @property
    def say_id(self) -> str:
        """Displays the employee's id."""
        return f"my id is {self.employee_id}"

    @property
    def say_email(self) -> str:
        """Displays the employee's email"""
        return f"my email is {self.email_address}"


@dataclass(kw_only=True)
class Worker(Employee):
    """Worker class"""

    @property
    def say_id_and_role(self):
        """Adds a role of the worker."""
        return f"{super().say_id} and I am a {self.employee_role.value}"


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    @property
    def say_id_and_role(self):
        """Adds a role of the manager."""
        return f"{super().say_id} and I am a {self.employee_role.value}"


@dataclass(kw_only=True)
class Intern(Employee):
    """Intern class"""

    @property
    def say_id_and_role(self):
        """Adds a role of the intern."""
        return f"{super().say_id} and I am an {self.employee_role.value}"


class InstancesManager:
    """Holds the class instances"""

    worker1 = Worker(
        person_name="Mary Smith",
        person_age=30,
        employee_role=Role.WORKER,
    )
    worker2 = Worker(
        person_name="John Doe",
        person_age=35,
        employee_role=Role.WORKER,
    )
    manager1 = Manager(
        person_name="Brandon Smith",
        person_age=40,
        employee_role=Role.MANAGER,
    )
    manager2 = Manager(
        person_name="Markus Sextus",
        person_age=45,
        employee_role=Role.MANAGER,
    )

    intern1 = Intern(
        person_name="Jennifer Ivans", person_age=20, employee_role=Role.INTERN
    )
    intern2 = Intern(
        person_name="Brian Donahue", person_age=19, employee_role=Role.INTERN
    )


def main() -> None:
    """Main function"""

    worker1 = InstancesManager.worker1
    worker2 = InstancesManager.worker2

    workers = [worker1, worker2]

    for worker in workers:
        print(
            f"My name is {worker.person_name}, I am {worker.person_age} years old, {worker.say_email}, {worker.say_id_and_role}"
        )

    print()

    manager1 = InstancesManager.manager1
    manager2 = InstancesManager.manager2

    managers = [manager1, manager2]

    for manager in managers:
        print(
            f"My name is {manager.person_name}, I am {manager.person_age} years old, {manager.say_email}, {manager.say_id_and_role}"
        )

    print()

    intern1 = InstancesManager.intern1
    intern2 = InstancesManager.intern2

    interns = [intern1, intern2]

    for intern in interns:
        print(
            f"My name is {intern.person_name}, I am {intern.person_age} years old, {intern.say_email}, {intern.say_id_and_role}"
        )


if __name__ == "__main__":
    main()
