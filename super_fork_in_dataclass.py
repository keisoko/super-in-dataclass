"""
Fork of  the Codecademy OOP lesson on super() in dataclass syntax 
"""

from dataclasses import dataclass, field
from enum import StrEnum, auto
from uuid import uuid4


@dataclass(frozen=True)
class ConstantNamespace:
    """Constant namespace"""

    PAY_RAISE_RATE = 1.04


constant = ConstantNamespace()


def generate_id() -> str:
    """Helper function to generate id."""
    return uuid4().hex


class Role(StrEnum):
    """Employee roles."""

    WORKER = auto()
    INTERN = auto()
    DEVELOPER = auto()
    MANAGER = auto()


@dataclass(slots=True, kw_only=True)
class Employee:
    """Employee parent class."""

    person_name: str
    person_age: int
    employee_pay_amount: int
    employee_role: Role
    employee_id: str = field(init=False, default_factory=generate_id)
    employee_email: str = field(init=False)

    def __post_init__(self) -> None:
        """Initializes the employee's email."""
        email_username = self.person_name.casefold().split()
        if len(email_username) > 1:
            self.employee_email = f"{"_".join(email_username)}@company.com"
        else:    
            self.employee_email = f"{email_username[0]}@company.com"

    @property
    def display_id_and_role(self) -> str:
        """Returns the employee's id and role"""
        if self.employee_role.startswith(("a", "e", "i", "o", "u")):
            return (
                f"My id is {self.employee_id} and I am an {self.employee_role.value}."
            )
        return f"My id is {self.employee_id} and I am a {self.employee_role.value}."

    def apply_raise(self) -> None:
        """Applies the company raise rate to the employee's payment amount"""
        self.employee_pay_amount = int(
            self.employee_pay_amount * constant.PAY_RAISE_RATE
        )


@dataclass
class Developer(Employee):
    """Developer class"""

    programming_languages: list[str] = field(default_factory=list)

    def add_programming_language(self, new_language) -> None:
        """Adds a new language to the current list"""
        if new_language not in self.programming_languages:
            self.programming_languages.append(new_language)

    @property
    def display_programming_languages(self) -> str | list[str]:
        """Returns the list of programming languages"""
        return f"My programming languages are {self.programming_languages}"


@dataclass(kw_only=True)
class Manager(Employee):
    """Manager class"""

    managed_employees: list[str] = field(default_factory=list)

    def add_employee(self, new_employee) -> None:
        """Add a new employee to the managed_employees list."""
        if new_employee not in self.managed_employees:
            self.managed_employees.append(new_employee)


def about_employees(employee: Employee) -> None:
    """Employees info complication"""
    employee.apply_raise()
    print(
        f"My name is {employee.person_name} and I am {employee.person_age} years old."
    )
    print(f"My email address is {employee.employee_email}")
    print(f"My pay is ${employee.employee_pay_amount:,}.")
    print(employee.display_id_and_role)


def employees_output(
    employee1: Employee, employee2: Employee, employee3: Employee
) -> None:
    """Outputs class instances"""
    employees = [employee1, employee2, employee3]
    for employee in employees:
        about_employees(employee)
        print()


def display_supervised_employees(role: Role) -> str | None:
    """Returns which employees are supervised by which manager"""
    match role:
        case Role.WORKER:
            return f"The {Role.WORKER}s are supervised by {manager1.person_name}."
        case Role.INTERN:
            return f"The {Role.INTERN}s are supervised by {manager2.person_name}."
        case Role.DEVELOPER:
            return f"The {Role.DEVELOPER}s are supervised by {manager3.person_name}."


worker1 = Employee(
    person_name="Mary Smith",
    person_age=30,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
worker2 = Employee(
    person_name="John Doe",
    person_age=35,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
worker3 = Employee(
    person_name="Alexander Octavian",
    person_age=27,
    employee_pay_amount=50_000,
    employee_role=Role.WORKER,
)
intern1 = Employee(
    person_name="Jennifer Ivans",
    person_age=20,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
intern2 = Employee(
    person_name="Brian Donahue",
    person_age=19,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
intern3 = Employee(
    person_name="Bernard Johnson",
    person_age=22,
    employee_pay_amount=20_000,
    employee_role=Role.INTERN,
)
developer1 = Developer(
    person_name="Dima Goldner",
    person_age=53,
    employee_pay_amount=65_000,
    programming_languages=["Pythons", "HTML", "CSS", "JavaScript"],
    employee_role=Role.DEVELOPER,
)
developer2 = Developer(
    person_name="Bob Smith",
    person_age=35,
    employee_pay_amount=65_000,
    programming_languages=["Java", "C++", "Typescript", "Rust"],
    employee_role=Role.DEVELOPER,
)
developer3 = Developer(
    person_name="Mary Woodward",
    person_age=39,
    employee_pay_amount=65_000,
    programming_languages=["C#", "Python", "Kotlin", "SQL"],
    employee_role=Role.DEVELOPER,
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
manager3 = Manager(
    person_name="Mathew Clairmont",
    person_age=50,
    employee_pay_amount=90_000,
    managed_employees=[developer1.person_name, developer2.person_name],
    employee_role=Role.MANAGER,
)


def execute_main() -> None:
    """Main function to execute"""

    print()

    employees_output(worker1, worker2, worker3)
    employees_output(intern1, intern2, intern3)

    developer1.add_programming_language("Go")
    developer2.add_programming_language("Swift")
    developer3.add_programming_language("Ruby")

    developers = [developer1, developer2, developer3]
    sorted_developers = sorted(developers, key=lambda developer: developer.person_age)

    for developer in sorted_developers:
        about_employees(developer)
        print(developer.display_programming_languages, "\n")

    manager1.add_employee(worker3.person_name)
    manager2.add_employee(intern3.person_name)
    manager3.add_employee(developer3.person_name)

    managers = [manager1, manager2, manager3]

    for manager in managers:
        about_employees(manager)
        print()

    print(display_supervised_employees(Role.WORKER))
    print(display_supervised_employees(Role.INTERN))
    print(display_supervised_employees(Role.DEVELOPER))


if __name__ == "__main__":
    execute_main()
