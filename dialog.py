class Human:
    def __init__(self, name: str):
        """
        Создает объект класса Human.

        :param name: Имя человека.
        :type name: str
        """
        self.name = name

    def answer_question(self, question: str) -> None:
        """
        Выводит ответ на вопрос.

        :param question: Вопрос.
        :type question: str
        """
        print("Очень интересный вопрос! Не знаю.")


class Student(Human):
    def ask_question(self, someone: "Human", question: str) -> None:
        """
        Выводит вопрос собеседнику, а затем ответ на этот вопрос.

        :param someone: Собеседник.
        :type someone: Human
        :param question: Вопрос.
        :type question: str
        """
        print(f"{someone.name}, {question}")
        someone.answer_question(question)
        print()  # Разделительный print


class Curator(Human):
    def answer_question(self, question: str) -> None:
        """
        Выводит ответ на вопрос.

        :param question: Вопрос.
        :type question: str
        """
        if question == "мне грустненько, что делать?":
            print("Держись, всё получится. Хочешь видео с котиками?")
        else:
            super().answer_question(question)


class CodeReviewer(Human):
    def answer_question(self, question: str) -> None:
        """
        Выводит ответ на вопрос.

        :param question: Вопрос.
        :type question: str
        """
        if question == "что не так с моим проектом?":
            print("О, вопрос про проект, это я люблю.")
        else:
            super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question: str) -> None:
        """
        Выводит ответ на вопрос.

        :param question: Вопрос.
        :type question: str
        """
        if question == "мне грустненько, что делать?":
            print("Отдохни и возвращайся с вопросами по теории.")
        elif question == "как устроиться на работу питонистом?":
            print("Сейчас расскажу.")
        else:
            super().answer_question(question)


student = Student("Руслан")
curator = Curator("Марина")
code_reviewer = CodeReviewer("Евгений")
mentor = Mentor("Ира")
someone = Human("Виталя")

student.ask_question(curator, "мне грустненько, что делать?")
student.ask_question(mentor, "мне грустненько, что делать?")
student.ask_question(code_reviewer, "когда каникулы?")
student.ask_question(code_reviewer, "что не так с моим проектом?")
student.ask_question(someone, "как устроиться на работу питонистом?")
student.ask_question(mentor, "как устроиться на работу питонистом?")
