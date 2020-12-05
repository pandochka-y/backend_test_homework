class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно

    # доверить его родительскому классу

    def answer_question(self, question):

        print('Очень интересный вопрос! Не знаю')


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    def ask_question(Human, someone, question):
        print(f'{someone}, {question}')
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question

        # запросите ответ на вопрос у someone
        print()  # этот print выводит разделительную пустую строку
        super().answer_question()




class Curator(Human):
    def answer_question(self, question):
        for i in question:

        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса


# объявите и реализуйте классы CodeReviewer и Mentor
# следующий код менять не нужно, он работает, мы проверяли

student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')


friend = Human('Виталя')
student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')