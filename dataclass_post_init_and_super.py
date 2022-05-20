"""
Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with Enum class
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


@dataclass(slots=True)
class Employee:
    """Employee parent class."""

    person_name: str
    person_age: int
    employee_role: Role
    employee_id: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the employee's id."""
        self.employee_id = generate_id(length=8)

    @property
    def say_id_and_role(self) -> str:
        """Displays the employee's id and role."""

        return f"my id is {self.employee_id} and I am a {self.employee_role.value}."


@dataclass
class Worker(Employee):
    """Worker class"""

    @property
    def say_id_and_role(self) -> str:
        """Extends the parent say_id method"""
        return f"{super().say_id_and_role}"


class Manager(Employee):
    """Manager class"""

    @property
    def say_id_and_role(self) -> str:
        """Extends the parent say_id method"""
        return f"{super().say_id_and_role}"


class InstancesManager:
    """Holds the class instances"""

    worker1 = Worker(
        person_name="Mary",
        person_age=30,
        employee_role=Role.WORKER,
    )
    worker2 = Worker(
        person_name="John",
        person_age=35,
        employee_role=Role.WORKER,
    )
    manager1 = Manager(
        person_name="Brandon",
        person_age=40,
        employee_role=Role.MANAGER,
    )
    manager2 = Manager(
        person_name="Mark",
        person_age=45,
        employee_role=Role.MANAGER,
    )


def main() -> None:
    """Main function"""

    workers = [InstancesManager.worker1, InstancesManager.worker2]

    for worker in workers:
        print(
            f"My name is {worker.person_name}, I am {worker.person_age} years old, {worker.say_id_and_role}"
        )

    managers = [InstancesManager.manager1, InstancesManager.manager2]

    for manager in managers:
        print(
            f"My name is {manager.person_name}, I am {manager.person_age} years old, {manager.say_id_and_role}"
        )


if __name__ == "__main__":
    main()
