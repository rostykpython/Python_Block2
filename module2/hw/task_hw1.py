import re
from abc import ABC, abstractmethod
from collections import UserDict
from datetime import datetime
import task_hw2 as notes


class Field(ABC):
    @abstractmethod
    def show(self):
        pass


class NameInterface(Field, ABC):
    pass


class Name(NameInterface, ABC):
    def __init__(self, name):
        self.name = name

    def show(self):
        return f"{self.name}" if self.name else ""


class PhoneInterface(Field, ABC):
    @abstractmethod
    def change_phone(self, new_phone):
        pass


class Phone(PhoneInterface):
    def __init__(self, phone):
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        flag = False
        res = re.search(
            r"(\+?(38)?0(67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7})", phone
        )
        if res:
            flag = True
            self.__phone = res.group()
        if not flag:
            print("Incorrect phone!")

    def change_phone(self, new_phone):
        self.phone = new_phone

    def show(self):
        return f"{self.phone}"


class EmailInterface(Field, ABC):
    pass


class Email(EmailInterface):
    def __init__(self, email):
        self.email = email

    def show(self):
        return f"{self.email}"


class AddressInterface(Field, ABC):
    pass


class Address(AddressInterface):
    def __init__(self, address):
        self.address = address

    def show(self):
        return f"{self.address}"


class BirthdayInterface(Field, ABC):
    @abstractmethod
    def days_to_birthday(self):
        pass


class Birthday(BirthdayInterface):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    def show(self):
        return f"{self.birthday}"

    def days_to_birthday(self):
        if self.__birthday:
            date_now = datetime.now()
            self.__birthday = self.__birthday.replace(year=date_now.year)
            days_to_birthday = self.__birthday - date_now
            return (
                days_to_birthday.days
                if days_to_birthday.days >= 0
                else days_to_birthday + 365
            )


class Record:
    def __init__(self, name, phone, email, birthday, address):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.email = Email(email)
        self.address = Address(address)
        self.birthday = Birthday(birthday)

    def change_phone(self, new_phone):
        self.phone.change_phone(new_phone)

    def show(self):
        return [self.name, self.phone, self.email, self.birthday, self.address]


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.show()] = record

    def change_phone(self, new_phone, name):
        self.data[name.title()].phone.change_phone(new_phone)

    def show_all(self):
        for name, contact_info in self.data.items():
            output_text = f"{name}:"
            for contact in contact_info.show():
                output_text += f"{contact.show()},"
            print(output_text[:-1])


class Command(ABC):
    @abstractmethod
    def do(self, *args):
        pass

    def undo(self):
        pass


class AddressBookCommandAdd(Command):
    def __init__(self, address_book: AddressBook):
        self.address_book = address_book

    def do(self, *args):
        self.address_book.add_record(*args)


class AddressBookCommandPhone(Command):
    def __init__(self, address_book: AddressBook):
        self.address_book = address_book

    def do(self, phone, name):
        self.address_book.change_phone(new_phone=phone, name=name)


class AddressBookCommandShow(Command):
    def __init__(self, address_book: AddressBook):
        self.address_book = address_book

    def do(self, *args):
        self.address_book.show_all()


class CommandInvoker:
    def __init__(self, command: Command):
        self.command = command

    def invoke(self, *args):
        self.command.do(*args)


def find_command(command_name):
    if command_name == "add-contact":
        return AddressBookCommandAdd
    elif command_name == "show-contact":
        return AddressBookCommandShow
    elif command_name == "change-phone":
        return AddressBookCommandPhone
    elif command_name == "add-note":
        return notes.RecordBookCommandAddRecord
    elif command_name == "show-note":
        return notes.RecordBookCommandShow


def execute_invoke(main_object, *args, **kwargs):
    executing_command = find_command(command_name=kwargs["command_name"])
    invoked_command = executing_command(main_object)
    CommandInvoker(invoked_command).invoke(*args)


if __name__ == "__main__":
    main_address_book = AddressBook()
    main_record_book = notes.RecordBook()
    while True:
        console_command = input(": ").lower().split()
        if console_command[0] == "add-contact":
            execute_invoke(
                main_address_book,
                Record(
                    console_command[1].title(),
                    console_command[2],
                    console_command[3] if len(console_command) >= 4 else None,
                    console_command[4] if len(console_command) >= 5 else None,
                    " ".join(console_command[5:])
                    if len(console_command) >= 6
                    else None,
                ),
                command_name=console_command[0],
            )

        elif console_command[0] == "show-contact":
            execute_invoke(main_address_book, command_name=console_command[0])

        elif console_command[0] == "change-phone":
            execute_invoke(
                main_address_book,
                console_command[2],
                console_command[1],
                command_name=console_command[0],
            )

        elif console_command[0] == "add-note":
            execute_invoke(
                main_record_book,
                notes.NoteRecord(
                    console_command[1], console_command[2], console_command[3:]
                ),
                command_name=console_command[0],
            )

        elif console_command[0] == "show-note":
            execute_invoke(main_record_book, command_name=console_command[0])

        elif console_command[0] in ["good bye", "close", "exit", "."]:
            print("Good bye!")
            break
        else:
            print("try again!")
