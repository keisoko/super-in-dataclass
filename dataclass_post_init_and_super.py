"""
Codecademy Intermediate Python 3 OOP lesson on super() in dataclass syntax with Enum class
"""

from dataclasses import dataclass
from enum import Enum


class Role(Enum):
    """Employee roles."""

    WORKER = "Worker"
    MANAGER = "Manager"


@dataclass(kw_only=True)
class Employee:
    """Employee parent class."""

    new_id = 1
    name: str
    age: int
    employee_role: Role

    def __post_init__(self) -> None:
        """Increments the employee's id."""

        self.employee_id = Employee.new_id
        Employee.new_id += 1

    @property
    def say_id(self) -> str:
        """Displays the employee's id and role."""

        return f"my id is {self.employee_id} and I am a {self.employee_role.value}."


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    @property
    def say_id(self) -> str:
        """Extends the parent say_id method"""
        return f"{super().say_id}"


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
        print(f"My name is {worker.name}, I am {worker.age} years old, {worker.say_id}")

    managers = [manager1, manager2]

    for manager in managers:
        print(
            f"My name is {manager.name}, I am {manager.age} years old, {manager.say_id}"
        )


if __name__ == "__main__":
    main()
