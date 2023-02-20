class Student:
    def __init__(self, student_id: int, first_name: str, last_name: str, exam_scores=None):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def add_score(self, score):
        if 1 <= score <= 100:
            self.exam_scores.append(score)
            return self.exam_scores
        else:
            print('score is above 100 or eq 0')
            score = int(input('try another score, be careful: '))

    def show_scores(self):
        my_string = ''
        for element in self.exam_scores:
            element = str(element) + ' '
            my_string += element
        print(my_string)

    def score_average(self):
        score_summa = sum(self.exam_scores)
        numers_of_scores = len(self.exam_scores)
        try:
            average = score_summa / numers_of_scores
            return f'{round(average, 2)}'
        except:
            return f'Student {self.first_name} {self.last_name} failed hir(her) exam'

    def course_passed(self):
        if len(self.exam_scores) >= 3 and float(self.score_average()) > 60.0:
            return True
        else:
            return False

student_1 = Student(1, "John", "Doe")
student_1.add_score(100)
student_1.add_score(95)
student_1.show_scores()
print(student_1.score_average())
print(student_1.course_passed())

student_2 = Student(2, "Linda", "Jones")
student_2.add_score(25)
student_2.add_score(65)
student_2.add_score(80)
student_2.add_score(75)
student_2.show_scores()
print(student_2.score_average())
print(student_2.course_passed())

student_3 = Student(3, "Jason", "Kirk")
student_3.add_score(50)
student_3.add_score(60)
student_3.add_score(55)
student_3.show_scores()
print(student_3.score_average())
print(student_3.course_passed())

student_4 = Student(4, "Jane", "Doe")
student_4.add_score(95)
student_4.add_score(80)
student_4.add_score(100)
print(student_4.score_average())
print(student_4.course_passed())

student_5 = Student(5, "Jane", "Doe")
student_5.show_scores()
print(student_5.score_average())
print(student_5.course_passed())