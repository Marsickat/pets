class User:
    def __init__(self, name: str, phone: str):
        """
        Создает объект класса User.

        :param name: Имя пользователя.
        :type name: str
        :param phone: Номер телефона пользователя.
        :type phone: str
        """
        self.name = name
        self.phone = phone

    def show(self) -> None:
        """
        Выводит информацию о пользователе.
        """
        print(f"{self.name} ({self.phone})")


class Friend(User):
    def show(self):
        """
        Выводит информацию о друге.
        """
        print(f"Имя: {self.name} || Телефон: {self.phone}")


user = User("Виктор Гюго", "+33 1 42 72 10 16")
friend = Friend("Виктор Гюго", "+33 1 42 72 10 16")

user.show()
friend.show()
