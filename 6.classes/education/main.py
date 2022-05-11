from classes import Student, Reviewer, Lecturer


def average_rate(persons, course):
    all_rates = []
    for person in persons:
        if course in person.grades.keys():
            all_rates += person.grades[course]
    return round(sum(all_rates) / len(all_rates), 1)


def main():
    student1 = Student('Elon', 'Musk', 'male')
    student2 = Student('Mark', 'Zuckerberg', 'male')
    lecturer1 = Lecturer('Linus', 'Torvalds')
    lecturer2 = Lecturer('Michael', 'Cavotta')
    reviewer1 = Reviewer('James', 'Gosling')
    reviewer2 = Reviewer('Bjarne', 'Stroustrup')

    lecturer1.courses_attached += ['Python', 'C++']
    lecturer2.courses_attached += ['Python', 'Ruby']
    reviewer1.courses_attached += ['Python', 'C++']
    reviewer2.courses_attached += ['Python', 'Ruby']
    student1.courses_in_progress += ['Python', 'C++']
    student1.finished_courses += ['DevSecOps']
    student2.courses_in_progress += ['Python', 'Ruby']
    student2.finished_courses += ['DevSecOps']

    student1.rate_hw(lecturer1, 'Python', 10)
    student1.rate_hw(lecturer1, 'Python', 9)
    student1.rate_hw(lecturer1, 'Python', 10)
    student1.rate_hw(lecturer1, 'C++', 10)
    student1.rate_hw(lecturer1, 'C++', 9)

    student2.rate_hw(lecturer2, 'Python', 9)
    student2.rate_hw(lecturer2, 'Python', 7)
    student2.rate_hw(lecturer2, 'Python', 10)
    student2.rate_hw(lecturer2, 'Ruby', 7)
    student2.rate_hw(lecturer2, 'Ruby', 9)

    reviewer1.rate_hw(student1, 'Python', 10)
    reviewer1.rate_hw(student1, 'Python', 9)
    reviewer1.rate_hw(student1, 'Python', 8)
    reviewer1.rate_hw(student1, 'C++', 10)
    reviewer1.rate_hw(student1, 'C++', 10)

    reviewer2.rate_hw(student2, 'Python', 9)
    reviewer2.rate_hw(student2, 'Python', 10)
    reviewer2.rate_hw(student2, 'Python', 5)
    reviewer2.rate_hw(student2, 'Ruby', 10)
    reviewer2.rate_hw(student2, 'Ruby', 7)

    print(student1)
    print()

    print(student2)
    print()

    print(lecturer1)
    print()

    print(lecturer2)
    print()

    print(reviewer1)
    print()

    print(reviewer2)
    print()

    print(student1 == student2)
    print(student1 != student2)
    print(student1 <= student2)
    print(student1 >= student2)
    print(student1 > student2)
    print(student1 < student2)
    print()

    print(lecturer1 == lecturer2)
    print(lecturer1 != lecturer2)
    print(lecturer1 <= lecturer2)
    print(lecturer1 >= lecturer2)
    print(lecturer1 > lecturer2)
    print(lecturer1 < lecturer2)
    print()

    print(average_rate(Student.students, 'Python'))
    print(average_rate(Student.students, 'C++'))
    print(average_rate(Student.students, 'Ruby'))

    print(average_rate(Lecturer.lecturers, 'Python'))
    print(average_rate(Lecturer.lecturers, 'C++'))
    print(average_rate(Lecturer.lecturers, 'Ruby'))


if __name__ == '__main__':
    main()
