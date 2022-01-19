from base_options import session, Students, Groups
from random import randrange
import faker


Session = session()


def add_info_students():
    for i in range(1, 6):
        fake_name = faker.Faker().name()
        Session.add(Students(fake_name, randrange(1, 4)))
        Session.commit()


def add_info_groups():
    for i in range(1, 4):
        Session.add(Groups(0))
        Session.commit()


def add_students_group():
    std_instances = Session.query(Students).all()
    quantity_of_groups = {}
    for std_instance in std_instances:
        if std_instance.group_id in quantity_of_groups:
            quantity_of_groups[std_instance.group_id] += 1
        else:
            quantity_of_groups[std_instance.group_id] = 1
    grp_std = Session.query(Groups)
    for i in range(1, 4):
        grp_std.filter(Groups.id == i).update({Groups.students_quantity:quantity_of_groups[i]})
        Session.commit()


if __name__ == '__main__':
    add_students_group()