
class Employee:
    def __init__(self, emp_id, name, position, tasks=None):
        if not isinstance(emp_id, int):
            raise ValueError("Employee ID must be an integer.")
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(position, str):
            raise ValueError("Position must be a string.")
        if tasks is None:
            tasks = []
        elif not isinstance(tasks, list):
            raise ValueError("Tasks must be a list of strings.")
        else:
            for task in tasks:
                if not isinstance(task, str):
                    raise ValueError("Each task must be a string.")
        
        self._emp_id = emp_id
        self._name = name
        self._position = position
        self._tasks = tasks

    # Getters
    def get_emp_id(self):
        return self._emp_id

    def get_name(self):
        return self._name

    def get_position(self):
        return self._position

    def get_tasks(self):
        return self._tasks.copy()  # Return a copy to prevent direct manipulation

    # Setters
    def set_name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name

    def set_position(self, position):
        if not isinstance(position, str):
            raise ValueError("Position must be a string.")
        self._position = position

    # Las tareas se asignarán y quitarán por medio de estos métodos
    def add_task(self, task):
        if not isinstance(task, str):
            raise ValueError("Task must be a string.")
        self._tasks.append(task)

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
        else:
            raise ValueError("Task not found in the task list.")



# Testing 


def main():
    print("=================================================================")
    print("Test Case 1: Create an Employee.")
    print("=================================================================")
    employee1 = Employee(1, "John Doe", "Receptionist", 30000)

    if employee1.get_emp_id() == 1:
        print("Test PASS. The parameter emp_id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_name() == "John Doe":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_position() == "Receptionist":
        print("Test PASS. The parameter position has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if employee1.get_salary() == 30000:
        print("Test PASS. The parameter salary has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Update Employee's Position and Salary.")
    print("=================================================================")
    employee1.set_position("Manager")
    employee1.set_salary(50000)

    if employee1.get_position() == "Manager":
        print("Test PASS. The employee's position has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_position().")

    if employee1.get_salary() == 50000:
        print("Test PASS. The employee's salary has been correctly updated.")
    else:
        print("Test FAIL. Check the method set_salary().")

# Testing ejemplo
try:
    emp1 = Employee(101, "John Doe", "Recepcionista", ["Check-in", "Answer calls"])
    print(f"Employee {emp1.get_name()} - Position: {emp1.get_position()}")
    emp1.add_task("Manage reservations")
    print("Tasks:", emp1.get_tasks())
    emp1.remove_task("Check-in")
    print("Updated Tasks:", emp1.get_tasks())
except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
    main()
