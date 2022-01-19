import unittest.mock
from module_ORM.hw.hw_orm_main import main, create_session_db
from module_ORM.hw.base_hw import engine_address_book, AddressBook

session = create_session_db(engine_address_book)


class TestBot(unittest.TestCase):

    @unittest.mock.patch('builtins.input', side_effect=['add contact rostyslav +380682450080 14.06.2002 rostislavlitvinest@gmail.com', 'exit'])
    def test_adding_contact(self, mock):
        self.assertEqual(main(), None)
        add_book_obj = session.query(AddressBook).filter(AddressBook.name == 'rostyslav')
        self.assertEqual(add_book_obj.phone, '+380682450080')
        add_book_obj.delete()
