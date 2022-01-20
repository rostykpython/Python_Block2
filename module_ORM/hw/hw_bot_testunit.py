import unittest.mock
import io
from base_hw import engine_address_book, AddressBook, NoteBook
from hw_orm_main import main, create_session_db

session = create_session_db(engine_address_book)


class TestBot(unittest.TestCase):
    def test_printing_show_birthday(self):
        with unittest.mock.patch(
            "builtins.input",
            side_effect=["add contact natalya +380682560080 03.09.1999", "exit"],
        ) as mock:
            main()
        with unittest.mock.patch(
            "builtins.input", side_effect=["show birthday natalya", "exit"]
        ) as mock1:
            with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_std_out:
                main()
                self.assertEqual(
                    fake_std_out.getvalue(),
                    "User natalya and his/her birthday at 03.09.1999\n",
                )
        session.query(AddressBook).delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "add contact natalya +380682450080 14.06.2002 rostislavlitvinest@gmail.com",
            "exit",
        ],
    )
    def test_adding_and_deleting_contact(self, mock):
        self.assertEqual(main(), None)
        add_book_obj = session.query(AddressBook).filter(AddressBook.name == "natalya")
        self.assertEqual(add_book_obj.one().phone, "+380682450080")
        add_book_obj.delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=["add note title --note Test note --tag tag1 tag2 tag3", "exit"],
    )
    def test_adding_note(self, mock):
        self.assertEqual(main(), None)
        note_book_obj = session.query(NoteBook).filter(NoteBook.title == "title")
        self.assertEqual(note_book_obj.one().title, "title")
        self.assertEqual(note_book_obj.one().note, "test note")
        self.assertEqual(note_book_obj.one().tags, ["tag1", "tag2", "tag3"])
        note_book_obj.delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "add note title --note Test note --tag tag1 tag2 tag3",
            "add tag title tag4",
            "exit",
        ],
    )
    def test_adding_tags(self, mock):
        self.assertEqual(main(), None)
        note_book_obj = session.query(NoteBook).filter(NoteBook.title == "title")
        self.assertEqual(note_book_obj.one().tags, ["tag1", "tag2", "tag3", "tag4"])
        note_book_obj.delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=["add contact bohdan +380503387099", "show contact bohdan", "exit"],
    )
    def test_printing_show_contact(self, mock):
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_std_out:
            self.assertEqual(main(), None)
            self.assertEqual(
                fake_std_out.getvalue(),
                'If you entered the address and it has not added enter "street" before your '
                "address\n"
                "Name: bohdan, Phone: +380503387099, Email: None, Birthday: None\n",
            )
        session.query(AddressBook).delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "add contact roman +380682450080",
            "edit contact roman phone +380503734441",
            "exit",
        ],
    )
    def test_editing_phone(self, mock):
        self.assertEqual(main(), None)
        add_book_obj = session.query(AddressBook).filter_by(name="roman")
        self.assertEqual(add_book_obj.one().phone, "+380503734441")
        session.query(AddressBook).delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=[
            "add note title --note mytest 1",
            "edit note title --note test successful",
            "exit",
        ],
    )
    def test_editing_note(self, mock):
        self.assertEqual(main(), None)
        note_obj = session.query(NoteBook).filter_by(title="title")
        self.assertEqual(note_obj.one().note, "test successful")

    def test_search_tags(self):
        with unittest.mock.patch(
            "builtins.input",
            side_effect=["add note new --note new new new --tag tag1 tag2", "exit"],
        ) as mock:
            main()

        with unittest.mock.patch(
            "builtins.input", side_effect=["search tags tag1", "exit"]
        ) as mock1:
            with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_std_out:
                main()
                self.assertEqual(
                    fake_std_out.getvalue(),
                    "Title: new\nNote: new new new\nTags: ['tag1', 'tag2']\n",
                )
        session.query(NoteBook).delete()
        session.commit()

    def test_search_note(self):
        with unittest.mock.patch(
            "builtins.input", side_effect=["add note new_note --note new_note", "exit"]
        ) as mock:
            main()

        with unittest.mock.patch(
            "builtins.input", side_effect=["search note new_note", "exit"]
        ) as mock1:
            with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_std_out:
                main()
                self.assertEqual(
                    fake_std_out.getvalue(),
                    "Title: new_note\nNote: new_note\nTags: []\n",
                )
        session.query(NoteBook).delete()
        session.commit()

    @unittest.mock.patch(
        "builtins.input",
        side_effect=["add contact rostyk +380682450080", "show all", "exit"],
    )
    def test_printing_show_all(self, mock):
        with unittest.mock.patch("sys.stdout", new=io.StringIO()) as fake_std_out:
            self.assertEqual(main(), None)
            self.assertEqual(
                fake_std_out.getvalue(),
                'If you entered the address and it has not added enter "street" before your '
                "address\n"
                "Name: rostyk, Phone: +380682450080, Email: None, Birthday: None\n",
            )
        session.query(AddressBook).delete()
        session.commit()
