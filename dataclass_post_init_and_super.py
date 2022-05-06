"""
Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with Enum class
"""
import random
import string
from dataclasses import dataclass, field
from enum import Enum


def generate_id(length: int = 8) -> str:
    """Helper function to generate id."""
    return "".join(random.choices(string.ascii_uppercase, k=length))


class Role(Enum):
    """Employee roles."""

    WORKER = "Worker"
    MANAGER = "Manager"


@dataclass(kw_only=True)
class Employee:
    """Employee parent class."""

    name: str
    age: int
    employee_role: Role
    employee_id: str = field(init=False)

    def __post_init__(self) -> None:
        """Initialize the employee's id."""
        self.employee_id = generate_id()

    @property
    def say_id_and_role(self) -> str:
        """Displays the employee's id and role."""

        return f"my id is {self.employee_id} and I am a {self.employee_role.value}."


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    @property
    def say_id_and_role(self) -> str:
        """Extends the parent say_id method"""
        return f"{super().say_id_and_role}"


def main() -> None:
    """Main function"""

    worker1 = Employee(
        name="Mary",
        age=30,
        employee_role=Role.WORKER,
    )
    worker2 = Employee(
        name="John",
        age=35,
        employee_role=Role.WORKER,
    )
    manager1 = Manager(
        name="John",
        age=40,
        employee_role=Role.MANAGER,
    )
    manager2 = Manager(
        name="Mark",
        age=45,
        employee_role=Role.MANAGER,
    )

    workers = [worker1, worker2]

    for worker in workers:
        print(
            f"My name is {worker.name}, I am {worker.age} years old, {worker.say_id_and_role}"
        )

    managers = [manager1, manager2]

    for manager in managers:
        print(
            f"My name is {manager.name}, I am {manager.age} years old, {manager.say_id_and_role}"
        )


if __name__ == "__main__":
    main()
