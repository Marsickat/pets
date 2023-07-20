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


mike = Contact("Михаил Булгаков", "2-03-27", "Россия, Москва, Большая Пироговская, дом 35б, кв. 6", "15.05.1891")
vlad = Contact("Владимир Маяковский", "73-88", "Россия, Москва, Лубянский проезд, д. 3, кв. 6", "19.07.1893")


def print_contact():
    """
    Выводит информацию о контактах.
    """
    print(f"{mike.name} - адрес: {mike.address}, телефон: {mike.phone}, день рождения: {mike.birthday}")
    print(f"{vlad.name} - адрес: {vlad.address}, телефон: {vlad.phone}, день рождения: {vlad.birthday}")


mike.address = "Россия, Москва, Нащокинский переулок, дом 3, кв. 44"
mike.phone = "К-058-67"

vlad.address = "Россия, Москва, Гендриков переулок, дом 15, кв. 5"
vlad.phone = "2-35-71"

print_contact()
