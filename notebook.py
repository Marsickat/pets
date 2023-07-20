class Contact:
    def __init__(self, name: str, phone: str, address: str, birthday: str):
        """
        Создает новый объект класса Contact.

        Параметры:
            name (str): Имя контакта.
            phone (str): Номер телефона контакта.
            address (str): Адрес контакта.
            birthday (str): Дата рождения контакта.
        """
        self.name = name
        self.phone = phone
        self.address = address
        self.birthday = birthday

    def show_contact(self) -> None:
        """
        Выводит информацию о контактах.
        """
        print(f"{self.name} - адрес: {self.address}, телефон: {self.phone}, день рождения: {self.birthday}")


mike = Contact("Михаил Булгаков", "2-03-27", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6", "15.05.1891")
vlad = Contact("Владимир Маяковский", "73-88", "Россия, Москва, Лубянский проезд, д. 3, кв. 6", "19.07.1893")

mike.show_contact()
vlad.show_contact()
