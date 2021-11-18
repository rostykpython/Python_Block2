from module_ORM.hw.base_hw import Session_address_book, Base, engine_address_book
import re
from sqlalchemy import any_
from datetime import datetime
from base_hw import AddressBook, NoteBook


def check_pattern(patterns, inst):
    patterns_list = []
    for pattern in patterns:
        found_text = re.search(pattern, inst)
        try:
            if len(found_text.group()) == len(inst):
                patterns_list.append((bool(found_text), inst))
        except AttributeError:
            patterns_list.append((False, None))

    return patterns_list


def field_address_book(obj):
    if obj == 'name':
        return AddressBook.name
    elif obj == 'phone':
        return AddressBook.phone
    elif obj == 'email':
        return AddressBook.email
    elif obj == 'birthday':
        return AddressBook.birthday
    elif obj == 'address':
        return AddressBook.address


def find_instance(instance: str) -> tuple:

    pattern_phone = '^\+?(38)?0(44|67|68|96|97|98|50|66|95|99|63|73|93|89|94)\d{7}$'
    pattern_email = '\w+@\w+.(com|net|ua|ru)'
    pattern_birthday = '\d{2}.\d{2}.\d{2,4}'

    patterns_group = [pattern_phone, pattern_email, pattern_birthday]

    patterns_list = check_pattern(patterns_group, instance)

    if instance.isalpha() and '@' not in instance:
        return 'name', instance
    elif patterns_list[0][0] and len(patterns_list[0][1]) == len(instance):
        return 'phone', instance
    elif patterns_list[1][0] and len(patterns_list[1][1]) == len(instance):
        return 'email', instance
    elif patterns_list[2][0] and len(patterns_list[2][1]) == len(instance):
        return 'birthday', instance
    return None, None


def main():
    print(f"COMMAND LINE INTERFACE\nYour Personal Assistant\n" + "=" * 23)

    Base.metadata.create_all(engine_address_book)
    Base.metadata.bind = engine_address_book
    session = Session_address_book()
    add_book = {
        'name': None,
        'phone': None,
        'email': None,
        'birthday': None,
        'address': None,
    }
    while True:
        command = input("Enter your command\n>> ").lower()
        sep_command = command.split(" ")
        if sep_command[0] == "add" and sep_command[1] == "contact":
            for item in sep_command[2:]:
                if item in ['st.', 'street', 'st']:
                    st_ind = sep_command.index(item)
                    address_user = ' '.join(sep_command[st_ind:])
                    add_book['address'] = address_user
                    continue
                inst_specs = find_instance(item)
                if inst_specs[0] in add_book.keys() and add_book[inst_specs[0]] is None:
                    add_book[inst_specs[0]] = inst_specs[1]
            if not add_book['address']:
                print('If you entered the address and it has not added enter "street" before your address')
            session.add(AddressBook(*add_book.values()))

        elif sep_command[0] == "add" and sep_command[1] == "note":
            tag_ind = sep_command.index('--tag') if '--tag' in sep_command else 0
            try:
                note_ind = sep_command.index('--note')
                if not tag_ind:
                    note_text = ' '.join(sep_command[note_ind + 1:])
                else:
                    note_text = ' '.join(sep_command[note_ind + 1:tag_ind])
                tags = []
            except IndexError:
                print('You need to do enter your note with flag "--note"')
                continue
            if tag_ind:
                tags = sep_command[tag_ind + 1:]

            print(f'Title: {sep_command[2]}, Note: {note_text}, Tags: {tags})')

            new_note = NoteBook(sep_command[2], note_text, tags, datetime.now().date())
            session.add(new_note)

        elif sep_command[0] == "add" and sep_command[1] == "tag":
            note = session.query(NoteBook).filter(NoteBook.title == sep_command[2]).one()
            note.tags.extend(sep_command[3:])
            session.query(NoteBook).filter(NoteBook.title == sep_command[2]).update({NoteBook.tags: note.tags})

        elif sep_command[0] == "show" and sep_command[1] == "contact":
            user_data = session.query(AddressBook).filter_by(name=sep_command[2])
            for u in user_data:
                print(u)

        elif sep_command[0] == "show" and sep_command[1] == "birthday":
            for user in session.query(AddressBook).filter(AddressBook.name == sep_command[2]):
                print(f'User {user.name} and his/her birthday at {user.birthday}')

        elif sep_command[0] == "show" and sep_command[1] == "all":
            for user in session.query(AddressBook).all():
                print(user)

        elif sep_command[0] == "show" and sep_command[1] == "notes":
            for note in session.query(NoteBook).all():
                print(note)
        elif sep_command[0] == "edit" and sep_command[1] == "contact":
            if len(sep_command) < 5:
                print(f'Your query was not correct\nTry again!')
                continue
            if sep_command[3] not in add_book.keys():
                print(f'Address book do not have such field as {sep_command[3]}\nTry again!')
                continue

            address_data = session.query(AddressBook).filter(AddressBook.name == sep_command[2])

            with address_data.one() as contact_data:
                contact_data[sep_command[3]] = ' '.join(sep_command[4:])

            address_data.update({field_address_book(sep_command[3]): contact_data[sep_command[3]]})

        elif sep_command[0] == "edit" and sep_command[1] == "note":
            note_ind = sep_command.index('--note') if '--note' in sep_command else None
            if not note_ind:
                print('You have to put flag "--note" in your line otherwise this command would not work!')
                continue
            session.query(NoteBook).filter(NoteBook.title == sep_command[2]).update(
                {NoteBook.note: ' '.join(sep_command[note_ind + 1:])})

        elif sep_command[0] == "search" and sep_command[1] == "tags":
            for note in session.query(NoteBook).filter(any_(NoteBook.tags) == sep_command[2]):
                print(note)

        elif sep_command[0] == "search" and sep_command[1] == "note":
            for note in session.query(NoteBook).filter(NoteBook.title == sep_command[2]):
                print(note)

        elif sep_command[0] == "delete" and sep_command[1] == "contact":
            session.query(AddressBook).filter(AddressBook.name == sep_command[2]).delete()

        elif sep_command[0] == "delete" and sep_command[1] == "note":
            session.query(NoteBook).filter(NoteBook.title == sep_command[2]).delete()

        elif command in ["good bye", "close", "exit"]:
            session.commit()
            session.close()
            break


if __name__ == '__main__':
    main()
