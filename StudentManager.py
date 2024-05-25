import sys


class Student:
    def __init__(self, id: int, name: str, age: int, sex: str, GPA: float) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.sex = sex
        self.GPA = GPA

    def show(self):
        print(
            f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Sex: {self.sex}, GPA: {self.GPA}"
        )


class StudentManager:
    num_students = 0

    def __init__(self) -> None:
        self.students = []

    def add(self, student: Student):
        self.students.append(student)
        self.num_students += 1

    def show(self):
        print("".center(50, "="))
        for i, student in enumerate(self.students):
            print(
                f"{i}. ID: {student.id}, Name: {student.name}, Age: {student.age}, Sex: {student.sex}, GPA: {student.GPA}"
            )
        print("".center(50, "="))

    def search_id(self, id: int):
        for student in self.students:
            if student.id == id:
                print("Search found!")
                student.show()
                return None
        print("No student found!")

    def update(self, target_id, **kwargs):
        new_id = kwargs.get("id")
        new_name = kwargs.get("name")
        new_age = kwargs.get("age")
        new_sex = kwargs.get("sex")
        new_GPA = kwargs.get("GPA")

        for student in self.students:
            if target_id == student.id:
                if new_id is not None:
                    student.id = new_id
                if new_name is not None:
                    student.name = new_name
                if new_age is not None:
                    student.age = new_age
                if new_sex is not None:
                    student.sex = new_sex
                if new_GPA is not None:
                    student.GPA = new_GPA
                print("Successfully updated!")
                student.show()
                return
        print("No student found!")

    def remove_id(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                self.num_students -= 1
                print(f"Removed!")
                student.show()
                return
        print("No student is removed!")

    def sort(self, order: str):
        if self.num_students == 0:
            print("No student found! Unable to sort!")
            return
        
        if order == "name":
            self.students = sorted(self.students, key=lambda student: student.name)

        elif order == "GPA":
            self.students = sorted(
                self.students, key=lambda student: student.GPA, reverse=True
            )
        else:
            print("Invalid order! Please enter order='name' or order='GPA'!")

    def isPresent(self, **kwargs):
        id = kwargs.get("id")
        name = kwargs.get("name")
        age = kwargs.get("age")
        sex = kwargs.get("sex")
        GPA = kwargs.get("GPA")

        for student in self.students:
            if (
                student.id == id
                or student.name == name
                or student.age == age
                or student.sex == sex
                or student.GPA == GPA
            ):
                return True
        return False


def test():
    student_1 = Student(21020533, "Thai", 21, "Male", 3.3)
    student_2 = Student(21020534, "Max", 23, "Male", 3.5)
    student_3 = Student(21020535, "Michelle", 19, "Female", 3.0)
    manager = StudentManager()
    manager.add(student_1)
    manager.add(student_2)
    manager.add(student_3)
    manager.show()
    manager.search_id(21020533)
    manager.update(21020534, name="Speed")
    manager.remove_id(21020533)
    manager.sort("name")
    manager.show()


if __name__ == "__main__":
    manager = StudentManager()
    print("Please choose the following options! (e.g. 1, 2 or 3)")
    print("".center(50, "="))
    print("1. Add student")
    print("2. Show students")
    print("3. Search student ID")
    print("4. Update student info based on ID")
    print("5. Remove student")
    print("6. Sort students based on name or GPA")
    print("7. Exit program")
    print("".center(50, "="))
    while True:
        print()
        user_input = input("Your option: ")
        print()
        option = int(user_input) if user_input.isdigit() else None
        if option is None:
            print("Invalid option!")
            continue

        if option == 7:
            print("EXITED!")
            sys.exit()

        if option == 1:
            print(
                "Please enter student's information in the following format: (id,name,age,sex,gpa) (NO SPACES BETWEEN)!"
            )
            (id, name, age, sex, gpa) = input("--> ").split(",")
            id, age, gpa = int(id), int(age), float(gpa)
            student = Student(id, name, age, sex, gpa)
            print("Added 1 student!")
            student.show()
            manager.add(student)

        if option == 2:
            if manager.num_students == 0:
                print("No students found")
            else:
                manager.show()

        if option == 3:
            search_id = input("Enter ID: ")
            id = int(search_id) if search_id.isdigit() else None
            if id is None:
                print("Invalid ID!")
                continue
            manager.search_id(id)

        if option == 4:
            search_id = input("Enter ID: ")
            target_id = int(search_id) if search_id.isdigit() else None
            if target_id is None:
                print("Invalid ID!")
                continue
            if not manager.isPresent(id=id):
                print("Student's ID not found!")
                continue
            print(
                "Enter values you want to change. E.g. id=21020533,name='Thai',age=21,sex='Male',GPA=3.3 (NO SPACES BETWEEN)!"
            )

            changes = input("--> ").split(",")
            temp = {key: None for key in ("id", "name", "age", "sex", "GPA")}
            for change in changes:
                key, value = change.split("=")
                if key in ["id", "age"]:
                    value = int(value)
                if key == "GPA":
                    value = float(value)
                temp[key] = value

            manager.update(
                target_id,
                id=temp.get("id"),
                name=temp.get("name"),
                age=temp.get("age"),
                sex=temp.get("sex"),
                GPA=temp.get("GPA"),
            )

        if option == 5:
            remove_id = input("Enter ID: ")
            id = int(remove_id) if remove_id.isdigit() else None
            if id is None:
                print("Invalid ID!")
                continue
            if not manager.isPresent(id=id):
                print("Student's ID not found!")
                continue
            manager.remove_id(id)
            
        if option == 6:
            order = input("Enter 'name' or 'GPA': ").strip()
            manager.sort(order)
                