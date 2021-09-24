from abc import ABC, abstractmethod
from collections import UserDict


class Field(ABC):
    @abstractmethod
    def show(self):
        pass


class AbstractRecord(ABC):
    @abstractmethod
    def change_note(self, *args, **kwargs):
        pass

    @abstractmethod
    def change_title(self, *args, **kwargs):
        pass

    @abstractmethod
    def add_tags(self, *args, **kwargs):
        pass

    @abstractmethod
    def del_tags(self, *args, **kwargs):
        pass


class Note(Field):
    def __init__(self, note):
        self.note = note

    def change_note(self, new_text):
        self.note = new_text

    def show(self):
        return self.note


class Tag(Field):
    def __init__(self, tags=None):
        if tags is None:
            tags = []
        self.tags = tags

    def add_tag(self, new_tags: list):
        self.tags.extend(new_tags)

    def del_tags(self, tags: list):
        for tag in tags:
            self.tags.remove(tag)

    def show(self):
        return self.tags


class Title(Field):
    def __init__(self, title):
        self.title = title

    def change_title(self, new_title):
        self.title = new_title

    def show(self):
        return self.title


class NoteRecord(AbstractRecord):
    def __init__(self, title, note, tags):
        self.title = Title(title)
        self.note = Note(note)
        self.tags = Tag(tags)

    def change_note(self, new_note):
        self.note.change_note(new_note)

    def change_title(self, new_title):
        self.title.change_title(new_title)

    def add_tags(self, new_tags):
        self.tags.add_tag(new_tags)

    def del_tags(self, tags):
        self.tags.del_tags(tags)

    def give_items(self):
        return [self.title, self.note, self.tags]


class RecordBook(UserDict, AbstractRecord):
    def add_record(self, record: NoteRecord):
        self.data[record.title.title] = record

    def change_note(self, new_note, title):
        self.data[title].change_note(new_note)

    def change_title(self, new_title, title):
        self.data[title].change_title(new_title)

    def add_tags(self, new_tags, title):
        self.data[title].add_tags(new_tags)

    def del_tags(self, tags, title):
        self.data[title].del_tags(tags)

    def show(self):
        for title, record in self.data.items():
            note_to_print = ''
            for i in record.give_items():
                note_to_print += f'{i.show()}'
            print(note_to_print)


class Command(ABC):
    @abstractmethod
    def do(self, *args):
        pass

    def undo(self):
        pass


class RecordBookCommandAddRecord(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.add_record(*args)


class RecordBookCommandChangeNote(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.change_note(*args)


class RecordBookCommandChangeTitle(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.change_title(*args)


class RecordBookCommandAddTags(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.add_tags(*args)


class RecordBookCommandDelTags(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.del_tags(*args)


class RecordBookCommandShow(Command):
    def __init__(self, record_book: RecordBook):
        self.record_book = record_book

    def do(self, *args):
        self.record_book.show()


class CommandInvoker:
    def __init__(self, command: Command):
        self.command = command

    def invoke(self, *args):
        self.command.do(*args)
