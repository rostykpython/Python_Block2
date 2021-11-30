import re
from pymongo import MongoClient


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
    add_book = {
        'name': None,
        'phone': None,
        'email': None,
        'birthday': None,
        'address': None,
    }
    client = MongoClient()
    db_address_book = client.address_book
    db_note_book = client.note_book
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
            db_address_book.contact_book.insert_one(add_book)

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

            db_note_book.notes.insert_one({'title': sep_command[2], 'note': note_text, 'tag': tags})

        elif sep_command[0] == "add" and sep_command[1] == "tag":
            db_note_book.notes.update_one({'title': sep_command[2]}, {'$push': {'tag': {'$each': sep_command[3:]}}})

        elif sep_command[0] == "show" and sep_command[1] == "contact":
            contact_data = db_address_book.contact_book.find({'name': sep_command[2]})
            for contact in contact_data:
                print('{}, {}, {}, {}, {}, {}'.format(*contact.values()))

        elif sep_command[0] == "show" and sep_command[1] == "birthday":
            birthday = db_address_book.contact_book.find({'name': sep_command[2]}, {'birthday': 1, '_id': 0})
            print(list(birthday)[0])

        elif sep_command[0] == "show" and sep_command[1] == "all":
            for contact in db_address_book.contact_book.find():
                print(contact)

        elif sep_command[0] == "show" and sep_command[1] == "notes":
            for note in db_note_book.notes.find():
                print(note)

        elif sep_command[0] == "edit" and sep_command[1] == "contact":
            if len(sep_command) < 5:
                print(f'Your query was not correct\nTry again!')
                continue
            if sep_command[3] not in add_book.keys():
                print(f'Address book do not have such field as {sep_command[3]}\nTry again!')
                continue

            db_address_book.contact_book.update_one({'name': sep_command[2]},
                                                    {'$set': {sep_command[3]: ' '.join(sep_command[4:])}})

        elif sep_command[0] == "edit" and sep_command[1] == "note":
            note_ind = sep_command.index('--note') if '--note' in sep_command else None
            if not note_ind:
                print('You have to put flag "--note" in your line otherwise this command would not work!')
                continue
            db_note_book.notes.update_one({'title': sep_command[2]},
                                          {'$set': {'note': ' '.join(sep_command[note_ind + 1:])}})

        elif sep_command[0] == "search" and sep_command[1] == "tags":
            for note in db_note_book.notes.find({'tag': {'$in': sep_command[2:]}}):
                print(note)

        elif sep_command[0] == "search" and sep_command[1] == "note":
            result = db_note_book.notes.find({'title': sep_command[2]})
            print(list(result)[0])
        elif sep_command[0] == "delete" and sep_command[1] == "contact":
            db_address_book.contact_book.remove({'name': sep_command[2]})

        elif sep_command[0] == "delete" and sep_command[1] == "note":
            db_note_book.notes.remove({'title': sep_command[2]})

        elif command in ["good bye", "close", "exit", '.']:
            break


if __name__ == '__main__':
    main()
