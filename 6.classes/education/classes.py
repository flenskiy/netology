class Student:
    students = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.students.append(self)

    def __str__(self):
        courses_in_progress = ', '.join(map(str, self.courses_in_progress))
        finished_courses = ', '.join(map(str, self.finished_courses))
        average_rate = self.__average_rate()
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {average_rate}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\n' \
               f'Завершенные курсы: {finished_courses}'

    def __eq__(self, other):
        return self.__average_rate() == other

    def __ne__(self, other):
        return self.__average_rate() != other

    def __ge__(self, other):
        return self.__average_rate() <= other

    def __le__(self, other):
        return self.__average_rate() >= other

    def __gt__(self, other):
        return self.__average_rate() > other

    def __lt__(self, other):
        return self.__average_rate() < other

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __average_rate(self):
        all_rates = []
        for grades in self.grades.values():
            all_rates += grades
        return round(sum(all_rates) / len(all_rates), 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    lecturers = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.lecturers.append(self)

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.__average_rate()}'

    def __average_rate(self):
        all_rates = []
        for grades in self.grades.values():
            all_rates += grades
        return round(sum(all_rates) / len(all_rates), 1)

    def __eq__(self, other):
        return self.__average_rate() == other

    def __ne__(self, other):
        return self.__average_rate() != other

    def __ge__(self, other):
        return self.__average_rate() <= other

    def __le__(self, other):
        return self.__average_rate() >= other

    def __gt__(self, other):
        return self.__average_rate() > other

    def __lt__(self, other):
        return self.__average_rate() < other
