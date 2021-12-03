from hw_app import app, db
from datetime import datetime
from flask import render_template, request, redirect, url_for
from hw_app.forms import AddressBookForm, NoteForm
from models import AddressBook, NoteBook


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/address', methods=['GET', 'POST'])
def address():

    form = AddressBookForm()

    if request.method == 'POST':
        data = request.form
        post = AddressBook(data['name'], data['phone'], data['email'], data['birthday'], data['street'])
        db.session.add(post)
        db.session.commit()
        db_data = AddressBook.query.all()
    elif request.method == 'GET':
        db_data = AddressBook.query.all()

    return render_template('address.html', form=form, data=db_data)


@app.route('/address/<int:address_book_id>')
def contact(address_book_id):
    contact = AddressBook.query.get_or_404(address_book_id)
    return render_template('contact.html', contact=contact)


@app.route('/address/<int:address_book_id>/delete', methods=['GET', 'POST'])
def contact_delete(address_book_id):
    contact = AddressBook.query.get_or_404(address_book_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('address'))


@app.route('/address/<int:address_book_id>/update', methods=['GET', 'POST'])
def contact_update(address_book_id):
    contact = AddressBook.query.get(address_book_id)
    form = AddressBookForm(obj=contact)

    if request.method == 'POST':
        contact.name = form.data['name']
        contact.phone = form.data['phone']
        contact.email = form.data['email']
        contact.birthday = form.data['birthday']
        contact.street = form.data['street']
        db.session.commit()
        return redirect(url_for('address'))
    return render_template('address.html', form=form)


@app.route('/notes', methods=['GET', 'POST'])
def notes():
    form = NoteForm()

    if request.method == 'POST':
        data = form.data
        tags = [tag['tag'] for tag in data['tags'] if tag['tag']]
        post = NoteBook(data['title'], data['note'], tags, datetime.now().isoformat())
        db.session.add(post)
        db.session.commit()

    db_data = NoteBook.query.all()
    
    return render_template('notes.html', form=form, db_data=db_data)


@app.route('/notes/<int:note_id>', methods=['GET', 'POST'])
def note(note_id):
    note = NoteBook.query.get_or_404(note_id)
    tags = '; '.join(note.tags)
    return render_template('note.html', note=note, tags=tags)


@app.route('/notes/<int:note_id>/delete', methods=['GET', 'POST'])
def note_delete(note_id):
    note = NoteBook.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('notes'))


@app.route('/notes/<int:note_id>/update', methods=['GET', 'POST'])
def note_update(note_id):
    note = NoteBook.query.get(note_id)
    form = NoteForm(obj=note)

    if request.method == 'POST':
        note.title = form.data['title']
        note.note = form.data['note']
        note.tags = [tag['tag'] for tag in form.data['tags'] if tag['tag']]
        db.session.commit()
        return redirect(url_for('notes'))
    return render_template('notes.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
